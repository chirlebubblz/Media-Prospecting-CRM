import csv
from src.crm.tracker import LeadTracker

tracker = LeadTracker()

# Add the two booked wins
tracker.add_or_update_lead({
    "id": "rethink_productivity",
    "name": "ReThink Productivity Podcast",
    "host": "Simon Hedaux",
    "genre": "Operations & Productivity",
    "contact_email": "simon@rethinkproductivity.co.uk",
    "website": "https://rethinkproductivity.co.uk/",
    "apple_url": "https://podcasts.apple.com/us/podcast/rethink-productivity-podcast/id1506790837",
    "status": "Booked",
    "pitch_angle": "Fraud as an operational productivity & margin drain",
    "notes": "Booked on show! 7 years, 335 eps, 19k reach. Show notes with hyperlinks."
})

tracker.add_or_update_lead({
    "id": "founders_podcast_uk",
    "name": "Founders Podcast",
    "host": "Ash Lonare",
    "genre": "Startups & Leadership",
    "contact_email": "ash@founderspodcast.uk",
    "website": "https://www.founderspodcast.uk/",
    "apple_url": "https://podcasts.apple.com/us/podcast/founders-podcast/id1704344895",
    "status": "Booked",
    "pitch_angle": "Founder Risk, Governance Traps & Due Diligence Blindspots",
    "notes": "Booked on show! 3 years, 175 eps, top 10% global ranking. Video interview on YouTube."
})

# Add the 8 verified matching shows
new_shows = [
    {
        "id": "the_operations_room",
        "name": "The Operations Room - A podcast for COOs",
        "host": "Beth Kelly & Brandon Hickie",
        "genre": "Operations & Executive Leadership",
        "website": "https://operationsroom.fm/",
        "feed_url": "https://feeds.buzzsprout.com/2141569.rss",
        "pitch_angle": "Fraud & Process Leakage as COO Margin Killers",
        "notes": "Top COO show. Target angle: Internal friction, shadow workflows, and operational loss."
    },
    {
        "id": "secret_leaders",
        "name": "Secret Leaders",
        "host": "Dan Murray-Serter",
        "genre": "UK Business & High-Growth Founders",
        "website": "https://secretleaders.com/",
        "feed_url": "https://feeds.acast.com/public/shows/secretleaders",
        "pitch_angle": "The Abraham Wald Bomber Paradox in Scaling Startups",
        "notes": "Premier UK founder podcast (240+ eps). Highly aligned with Ash Lonare audience."
    },
    {
        "id": "practical_founders",
        "name": "Practical Founders Podcast",
        "host": "Greg Head",
        "genre": "Software & Scaleup Founders",
        "website": "https://practicalfounders.com/podcast/",
        "feed_url": "https://feeds.buzzsprout.com/1922578.rss",
        "contact_email": "greg@scalingpoint.com",
        "pitch_angle": "Why Fast Scaling Increases Behavioral Risk 67%",
        "notes": "216 episodes. Focus on building real enterprise value without reckless burn."
    },
    {
        "id": "riding_unicorns",
        "name": "Riding Unicorns",
        "host": "James Pringle & Hector Mason",
        "genre": "VC, Private Equity & Founder Diligence",
        "website": "https://www.ridingunicorns.co/",
        "feed_url": "https://feeds.acast.com/public/shows/riding-unicorns",
        "pitch_angle": "What VCs and Boards Miss in Early Stage Due Diligence",
        "notes": "Top UK tech and investment podcast. Perfect for Rupert's deal diligence hook."
    },
    {
        "id": "private_equity_podcast",
        "name": "The Private Equity Podcast",
        "host": "Lawson Hobbs",
        "genre": "Private Equity & M&A",
        "website": "https://privateequitypodcast.com/",
        "feed_url": "https://feeds.buzzsprout.com/1529525.rss",
        "pitch_angle": "M&A Due Diligence Catches Only 33% of True Risks",
        "notes": "Focus on PE operators and portco governance."
    },
    {
        "id": "money_maze_podcast",
        "name": "Money Maze Podcast",
        "host": "Oliver",
        "genre": "Finance & Asset Management",
        "website": "https://www.moneymazepodcast.com/",
        "feed_url": "https://feeds.buzzsprout.com/1126155.rss",
        "contact_email": "oliver@moneymazepodcast.com",
        "pitch_angle": "The Quantitative Trap: Why Smart Boards Audit the Wrong Signals",
        "notes": "245 episodes. Premier UK financial leadership show."
    },
    {
        "id": "permanent_podcast",
        "name": "Permanent Podcast",
        "host": "Permanent Equity Team",
        "genre": "Private Equity & Operations",
        "website": "https://permanentequity.com/",
        "feed_url": "https://adventur-es.libsyn.com/rss",
        "contact_email": "content@permanentequity.com",
        "pitch_angle": "How to Do Diligence Confidently Beyond 60-Page Checklists",
        "notes": "Long-term holding company and PE operators."
    },
    {
        "id": "scale_up_valley",
        "name": "Scale Up Valley Podcast",
        "host": "Mike Dias",
        "genre": "Scaleups & Executive Culture",
        "website": "https://scaleupvalley.com/",
        "feed_url": "https://anchor.fm/s/a35f0b0/podcast/rss",
        "pitch_angle": "Scaling Integrity & Psychological Safety in Fast Growth",
        "notes": "Covers high-growth leadership and organizational integrity."
    }
]

for s in new_shows:
    tracker.add_or_update_lead(s)

tracker.save()
print("LeadTracker updated with booked shows and verified new targets!")
