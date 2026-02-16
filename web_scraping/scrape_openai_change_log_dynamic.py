import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Reusable function to find the content block reliably
def find_stable_content(soup):
    try:
        # Try specific selector first
        # div = soup.select_one("#root > div.rl7uK > main > div > div > div > div > div > span > div > div > div")
        # if div:
        #     return div
        # Fallback: look inside <main> and find the first large text block
        main = soup.find("main")
        if main:
            for d in main.find_all("div"):
                if len(d.get_text(strip=True)) > 1500:
                    return d
    except Exception:
        pass
    return None

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

# Use the stable content finder
target_div = find_stable_content(soup)

# Extract and clean the text
if target_div:
    text = target_div.get_text(separator="\n", strip=True)
    text = re.sub(r'[\r\t\u200b]+', '', text)
else:
    text = "Content not found"

# Save to text file
with open("openai_changelog_dynamic.txt", "w", encoding="utf-8-sig") as f:
    f.write(text)

print("✅ OpenAI changelog content saved to 'openai_changelog_dynamic.txt'")

driver.quit()