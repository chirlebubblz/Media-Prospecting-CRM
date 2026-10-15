import requests
import re
import json

url = "https://docs.google.com/spreadsheets/d/1J9fgbNlszCL66w4p6cS_ImMob5GEMilHiZFgLnaPIF8/edit"
r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# Look for sheet titles and sheetId
pattern = r'\{\"sheetId\":(\d+),\"title\":\"([^\"]+)\"'
found = re.findall(pattern, r.text)
if not found:
    pattern2 = r'\[(\d+),\"([^\"]+)\",\d+,'
    found = re.findall(pattern2, r.text)

print("Sheets found:", found)

# Also check all lines in tab 286300149 for podcasts or media
csv_url = "https://docs.google.com/spreadsheets/d/1J9fgbNlszCL66w4p6cS_ImMob5GEMilHiZFgLnaPIF8/export?format=csv&gid=286300149"
r_csv = requests.get(csv_url, headers={"User-Agent": "Mozilla/5.0"})
with open("scraped_sheet_tab.csv", "w", encoding="utf-8") as f:
    f.write(r_csv.text)

print("Saved tab 286300149 to scraped_sheet_tab.csv")
