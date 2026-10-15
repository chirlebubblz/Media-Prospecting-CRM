import json
import os

LEADS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "leads.json"))

def fix_angles():
    if not os.path.exists(LEADS_PATH):
        print(f"Error: {LEADS_PATH} not found.")
        return

    with open(LEADS_PATH, "r", encoding="utf-8") as f:
        leads = json.load(f)

    # Specific bespoke angles for early anchor targets
    bespoke_angles = {
        "https://compliancepodcastnetwork.libsyn.com/rss": {
            "rupert_angle": "Whistleblower Hotline Paradox: Why 80% of Intake Reports Fail Before Investigation.",
            "talking_points": "• Why anonymous portals fail to provide psychological safety\n• DOJ evaluation of compliance programs: operationalizing behavioral data\n• The first 72 hours of an internal whistleblowing inquiry",
            "topic": "DOJ Guidelines, Corporate Integrity & Operational Compliance",
            "theme": "The flagship podcast network in corporate compliance, anti-corruption, and ethics."
        },
        "https://feeds.buzzsprout.com/791880.rss": {
            "rupert_angle": "The Quantitative Trap: Why Smart Boards Audit Returning Bombers (The 67% Behavioral Gap).",
            "talking_points": "• Abraham Wald's bomber paradox applied to corporate compliance\n• The 'Open Door' question that founders and boards fail to ask\n• Non-verbal triangulation in due diligence and crisis interviews",
            "topic": "Workplace Psychology, Behavioral Compliance & Human Decision Making",
            "theme": "Exploring why people do or don't do the right things, bringing behavioral science to compliance."
        },
        "https://complianceperspectives.libsyn.com/rss": {
            "rupert_angle": "Beyond the 33% Checklist: Transforming Annual Compliance Audits into Ground-Truth Risk Telemetry.",
            "talking_points": "• Why traditional annual surveys measure compliance comfort rather than reality\n• Harvesting weak signals of friction before an audit breach\n• Bridging the gap between written code of conduct and shopfloor incentives",
            "topic": "Practitioner Insights, Board Reporting & Risk Auditing",
            "theme": "Short, practical insights from top compliance practitioners worldwide on ethics programs and board reporting."
        },
        "https://feeds.buzzsprout.com/319614.rss": {
            "rupert_angle": "The Invisible Laundromat: How Qualitative Due Diligence Detects Transnational Financial Crime Before the Bank Flags It.",
            "talking_points": "• Why transaction monitoring algorithms miss structured operational fraud\n• Reading behavioral friction in high-risk foreign subsidiaries\n• Pre-deal intelligence: how to conduct human source due diligence without alerting bad actors",
            "topic": "Anti-Money Laundering (AML), Sanctions Evasion & Fraud Investigations",
            "theme": "In-depth discussions with leading minds in anti-money laundering (AML), sanctions, and anti-fraud."
        },
        "cci_publication": {
            "rupert_angle": "The Signal of Silence: Why a 'Clean' Hotline is a Board's Most Dangerous Metric.",
            "talking_points": "• The fallacy of zero reports: why silence signals organizational fear\n• Modernizing whistleblowing: moving from intake logs to risk telemetry\n• 5 qualitative questions every board member should ask the Head of Ethics",
            "topic": "Corporate Governance, Whistleblowing & Board Risk Oversight",
            "theme": "Leading independent media publisher and knowledge base for corporate compliance and ethics professionals."
        }
    }

    count = 0
    for lead_id, lead in leads.items():
        if lead_id in bespoke_angles:
            lead.update(bespoke_angles[lead_id])
            count += 1
            continue

        if not lead.get("rupert_angle") or lead.get("rupert_angle") == "Custom narrative hook pending.":
            t_lower = (lead.get("topic", "") + " " + lead.get("name", "") + " " + lead.get("genre", "") + " " + lead.get("description", "")).lower()

            if any(w in t_lower for w in ["productiv", "operat", "supply", "margin", "efficiency", "retail", "workforce", "coo"]):
                lead["rupert_angle"] = "Fraud as an Operational Productivity Drain — Why internal misconduct, process bypasses, and time theft destroy margins faster than supply chain inefficiencies."
                lead["talking_points"] = "• The hidden productivity cost of shadow workflows\n• Why employees bypass internal controls to 'get things done'\n• Turning compliance telemetry into operational margin protection"
            elif any(w in t_lower for w in ["founder", "startup", "scale", "venture", "entrepreneur", "tech"]):
                lead["rupert_angle"] = "Founder Blindspots & Due Diligence Traps — Why fast-growing startups face a 67% behavioral gap that spreadsheets fail to predict."
                lead["talking_points"] = "• Abraham Wald's bomber paradox: why boards only look at survivor metrics\n• The 'Open Door' myth in startup culture\n• What VCs fail to ask during pre-Series A/B due diligence"
            elif any(w in t_lower for w in ["equity", "m&a", "invest", "merger", "acquis", "deal", "portfolio"]):
                lead["rupert_angle"] = "M&A Due Diligence Catches Only 33% of True Risks: Why Deals Fail in Post-Merger Cultural Integration."
                lead["talking_points"] = "• The 'IBM Syndrome' in commercial due diligence: relying on checklists over human intelligence\n• Identifying operational fraud and margin leakage in newly acquired portcos\n• The 72-hour playbook for an internal investigation inside a portfolio asset"
            elif any(w in t_lower for w in ["fraud", "crime", "investigat", "forensic", "aml", "sanction"]):
                lead["rupert_angle"] = "The Transnational Fraud Blindspot: Why Sophisticated Bad Actors Always Circumvent Algorithmic Controls."
                lead["talking_points"] = "• Why transaction monitoring misses structured operational misconduct\n• The qualitative due diligence playbook for high-risk jurisdictions\n• The psychology of internal perpetrators: rationalization and pressure curves"
            else:
                lead["rupert_angle"] = "The Quantitative Trap: Why Smart Boards Audit the Wrong Signals — The 67% Behavioral Risk Gap."
                lead["talking_points"] = "• Abraham Wald's bomber paradox: why boards only audit clean 'returning planes'\n• The Signal of Silence: why zero whistleblower reports indicates fear, not integrity\n• Non-verbal triangulation in due diligence and executive friction"

            count += 1

    with open(LEADS_PATH, "w", encoding="utf-8") as f:
        json.dump(leads, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated bespoke strategic angles for {count} leads in {LEADS_PATH}!")

if __name__ == "__main__":
    fix_angles()
