"""
Prompt to scrape the leaderboard:

Write a web scraper using Python and BeautifulSoup.
Target: https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard
Rationale: Scrape the LLM performance details on the target page.
CSS selectors are as follows:
Leaaderboard table: body > main > div.mb-8 > div > div.container.m-auto.pb-8 > div > div.rounded-md.border.bg-white > div > table
Output: Save all the data in the leaderboard table in a CSV file
Additional Instructions: Handle character encoding and remove undesirable symbols in the output CSV.
"""
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

# The final URL that contains the real leaderboard
url = "https://artificialanalysis.ai/embed/llm-performance-leaderboard"

# Send GET request
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")

# Locate the leaderboard table
table = soup.find("table")
if table is None:
    raise Exception("Leaderboard table not found.")

# Extract headers
rows = table.find_all("tr")
headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]

# Extract data
data = []
for row in rows[1:]:
    cols = []
    for td in row.find_all("td"):
        # Check for image inside the cell
        img = td.find("img")
        if img and img.get("src"):
            # Get image filename from src URL
            img_name = img["src"].split("/")[-1]
            cols.append(img_name)
        else:
            # Otherwise just get cleaned text
            text = re.sub(r'[\n\r\t\u200b]+', '', td.get_text(strip=True))
            cols.append(text)
    if cols:
        data.append(cols)

# Save to CSV
df = pd.DataFrame(data, columns=headers)
df.to_csv("llm_leaderboard2.csv", index=False, encoding="utf-8-sig")

print("✅ LLM leaderboard data saved to 'llm_leaderboard.csv'")