#!/usr/bin/env python3
"""
Media Discovery & Outreach CLI
Discover, extract contact info, and track outreach for podcasts and shows.
"""

import argparse
import sys
from typing import Optional

from src.discovery.podcast_crawler import search_podcasts, search_preset_categories, DEFAULT_PRESET_QUERIES
from src.discovery.rss_extractor import enrich_from_rss
from src.crm.tracker import LeadTracker, CSV_PATH, JSON_PATH


def cmd_search(args):
    tracker = LeadTracker()
    results = []

    if args.presets:
        print(f"[*] Running auto-discovery across {len(DEFAULT_PRESET_QUERIES)} compliance, risk & finance presets...")
        results = search_preset_categories(limit_per_query=args.limit)
    else:
        query = args.query or "corporate compliance"
        print(f"[*] Searching podcasts for: '{query}' (limit: {args.limit})...")
        results = search_podcasts(query=query, limit=args.limit)

    print(f"[+] Found {len(results)} matching podcasts.")

    new_count = 0
    enriched_count = 0

    for i, show in enumerate(results, 1):
        name = show["name"]
        feed_url = show["feed_url"]
        print(f"[{i}/{len(results)}] {name} - {show.get('host', 'N/A')}")

        if args.enrich:
            print(f"     -> Inspecting RSS feed for contacts & episodes...")
            rss_data = enrich_from_rss(feed_url)
            show.update(rss_data)
            if show.get("contact_email"):
                print(f"     -> [CONTACT EMAIL FOUND]: {show['contact_email']}")
                enriched_count += 1
            if show.get("website"):
                print(f"     -> Website: {show['website']}")

        is_new = tracker.add_or_update_lead(show)
        if is_new:
            new_count += 1

    tracker.save()
    print("\n" + "=" * 60)
    print(f"[DONE] Processed {len(results)} shows.")
    print(f"       New leads added: {new_count}")
    if args.enrich:
        print(f"       Direct emails extracted: {enriched_count}")
    print(f"       Saved to: {CSV_PATH}")
    print(f"                 {JSON_PATH}")
    print("=" * 60)


def cmd_list(args):
    tracker = LeadTracker()
    leads = tracker.get_leads(status_filter=args.status)

    if args.emails_only:
        leads = [l for l in leads if l.get("contact_email")]

    if not leads:
        print("No leads found matching criteria. Run 'python cli.py search' to find shows.")
        return

    print(f"\nSaved Media Leads ({len(leads)} total):")
    print("-" * 90)
    print(f"{'#':<3} | {'Show Name':<35} | {'Host / Artist':<20} | {'Email':<24} | {'Status'}")
    print("-" * 90)

    for i, lead in enumerate(leads, 1):
        name = (lead.get("name") or "")[:33]
        host = (lead.get("host") or "")[:18]
        email = (lead.get("contact_email") or "—")[:22]
        status = lead.get("status", "Researching")
        print(f"{i:<3} | {name:<35} | {host:<20} | {email:<24} | {status}")

    print("-" * 90)


def cmd_inspect(args):
    tracker = LeadTracker()
    leads = tracker.get_leads()
    query = args.target.lower()

    matches = [l for l in leads if query in l.get("name", "").lower() or query in l.get("feed_url", "").lower()]
    if not matches:
        print(f"[!] No saved lead matched: '{args.target}'")
        return

    for show in matches:
        print("\n" + "=" * 70)
        print(f"SHOW: {show.get('name')}")
        print(f"Host: {show.get('host')}")
        print(f"Genre: {show.get('genre')}")
        print(f"Status: {show.get('status')}")
        print(f"Website: {show.get('website') or 'N/A'}")
        print(f"Apple Podcasts: {show.get('apple_url') or 'N/A'}")
        print(f"Primary Email: {show.get('contact_email') or 'None found'}")
        if show.get("all_emails"):
            print(f"All Extracted Emails: {', '.join(show['all_emails'])}")
        print(f"Pitch Angle: {show.get('pitch_angle') or 'Not set'}")
        print(f"Notes: {show.get('notes') or 'None'}")
        print(f"Feed URL: {show.get('feed_url')}")
        
        recent_eps = show.get("recent_episodes", [])
        if recent_eps:
            print("\nRecent Episodes:")
            for ep in recent_eps[:3]:
                print(f"  * {ep.get('title')} ({ep.get('date', '')[:16]})")
        print("=" * 70)


def cmd_update(args):
    tracker = LeadTracker()
    success = tracker.update_status(
        key_or_name=args.target,
        status=args.status,
        notes=args.notes or "",
        pitch_angle=args.angle or "",
    )
    if success:
        print(f"[+] Successfully updated status of '{args.target}' to '{args.status}'.")
    else:
        print(f"[!] Target '{args.target}' not found in database.")


def cmd_export(args):
    tracker = LeadTracker()
    leads = tracker.get_leads()
    out_path = args.output or "media_kit/discovered_leads.md"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Discovered Media Leads (Auto-Generated)\n\n")
        f.write(f"Total Leads: {len(leads)}\n\n")
        f.write("| # | Show Name | Host | Primary Email | Website | Status | Recent Episode |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
        for i, lead in enumerate(leads, 1):
            name = lead.get("name", "").replace("|", "-")
            host = lead.get("host", "").replace("|", "-")
            email = lead.get("contact_email") or "—"
            web = f"[Link]({lead['website']})" if lead.get("website") else "—"
            status = lead.get("status", "Researching")
            recent_sample = ""
            if lead.get("recent_episodes"):
                recent_sample = lead["recent_episodes"][0].get("title", "").replace("|", "-")[:45] + "..."
            f.write(f"| {i} | {name} | {host} | `{email}` | {web} | {status} | {recent_sample} |\n")

    print(f"[+] Exported {len(leads)} leads to: {out_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Media Outreach & Discovery Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")

    # Command: search
    p_search = subparsers.add_parser("search", help="Search podcast directories for compliance and risk shows")
    p_search.add_argument("--query", "-q", type=str, help="Search term (e.g. 'financial crime')")
    p_search.add_argument("--presets", action="store_true", help="Run search across all compliance/risk preset keywords")
    p_search.add_argument("--limit", "-l", type=int, default=10, help="Max results per search (default: 10)")
    p_search.add_argument("--enrich", action="store_true", help="Download RSS feeds to extract contact emails and recent episodes")

    # Command: list
    p_list = subparsers.add_parser("list", help="List discovered leads from local database")
    p_list.add_argument("--status", type=str, help="Filter by status (e.g. Researching, Pitched, Booked)")
    p_list.add_argument("--emails-only", action="store_true", help="Show only leads where a contact email was found")

    # Command: inspect
    p_inspect = subparsers.add_parser("inspect", help="Inspect details of a specific podcast lead")
    p_inspect.add_argument("target", type=str, help="Show name or feed URL snippet")

    # Command: update
    p_update = subparsers.add_parser("update", help="Update outreach status for a lead")
    p_update.add_argument("target", type=str, help="Show name to update")
    p_update.add_argument("--status", "-s", required=True, choices=["Researching", "Pitched", "Follow-up 1", "Follow-up 2", "Booked", "Declined"], help="New status")
    p_update.add_argument("--notes", "-n", type=str, help="Notes or follow-up details")
    p_update.add_argument("--angle", "-a", type=str, help="Pitch angle used")

    # Command: export
    p_export = subparsers.add_parser("export", help="Export leads to a Markdown summary table")
    p_export.add_argument("--output", "-o", type=str, default="media_kit/discovered_leads.md", help="Output file path")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "search":
        cmd_search(args)
    elif args.command == "list":
        cmd_list(args)
    elif args.command == "inspect":
        cmd_inspect(args)
    elif args.command == "update":
        cmd_update(args)
    elif args.command == "export":
        cmd_export(args)


if __name__ == "__main__":
    main()
