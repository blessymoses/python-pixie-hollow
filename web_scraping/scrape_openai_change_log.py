import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up headless Chrome
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# Load the OpenAI changelog page
url = "https://platform.openai.com/docs/changelog"
driver.get(url)

# Wait for JavaScript to render
time.sleep(5)

# Parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find the nested content div (changelog container)
target_div = soup.select_one("#root > div.rl7uK > main > div > div > div > div > div > span > div > div > div")

if target_div:
    text = target_div.get_text(separator="\n", strip=True)
    text = re.sub(r'[\r\t\u200b]+', '', text)
else:
    text = "Content not found"

# Save to text file
with open("openai_changelog.txt", "w", encoding="utf-8-sig") as f:
    f.write(text)

print("✅ OpenAI changelog content saved to 'openai_changelog.txt'")

driver.quit()