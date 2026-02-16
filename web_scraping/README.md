# Web Scrapers

## LLM Leaderboard Scraper

This is a simple Python script that scrapes the LLM performance leaderboard from the [Artificial Analysis Hugging Face Space](https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard), which embeds its content from [artificialanalysis.ai](https://artificialanalysis.ai/embed/llm-performance-leaderboard).

### 🔍 Purpose

To extract detailed performance metrics of various large language models (LLMs) from a dynamically embedded table and store the results in a clean CSV format.
- Sends a GET request to the embedded leaderboard page.
- Parses the HTML using BeautifulSoup.
- Identifies and extracts:
  - Table headers
  - Model data (text + embedded image filenames)
- Cleans and structures the data.
- Saves the result to a UTF-8 encoded CSV file named `llm_leaderboard2.csv`.

- This script targets the actual embedded leaderboard at `https://artificialanalysis.ai/embed/llm-performance-leaderboard` because the Hugging Face Space uses an iframe.
- Any images found in the table are captured by filename only, not downloaded.

### 🧰 Dependencies

- `requests`
- `beautifulsoup4`
- `pandas`

---
## 🧾 OpenAI Changelog Scraper (Dynamic Page)

This script uses **Selenium** and **BeautifulSoup** to scrape the changelog content from OpenAI’s dynamic documentation page:  
🔗 https://platform.openai.com/docs/changelog

The OpenAI changelog page is rendered using JavaScript (React), which means static scrapers like `requests + BeautifulSoup` won’t work. This script solves that by:

- Using **Selenium** to render the JavaScript.
- Using **BeautifulSoup** to parse and extract the content.
- Using a **fallback mechanism** to ensure scraping still works if CSS classes change.

### 🛠️ Features

- **Headless Browser**: Runs Chrome in headless mode for performance.
- **Dynamic Content Extraction**: Waits for JS to render.
- **Fallback Logic**: Attempts to find a large `<div>` inside `<main>` if the usual selector fails.
- **Text Cleaning**: Removes unwanted characters and whitespace.
- **File Output**: Saves extracted content to a UTF-8 encoded `.txt` file.

---