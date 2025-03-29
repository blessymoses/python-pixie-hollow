# LLM Leaderboard Scraper

This project is a simple Python script that scrapes the LLM performance leaderboard from the [Artificial Analysis Hugging Face Space](https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard), which embeds its content from [artificialanalysis.ai](https://artificialanalysis.ai/embed/llm-performance-leaderboard).

## 🔍 Purpose

To extract detailed performance metrics of various large language models (LLMs) from a dynamically embedded table and store the results in a clean CSV format.

## 🧠 What It Does

- Sends a GET request to the embedded leaderboard page.
- Parses the HTML using BeautifulSoup.
- Identifies and extracts:
  - Table headers
  - Model data (text + embedded image filenames)
- Cleans and structures the data.
- Saves the result to a UTF-8 encoded CSV file named `llm_leaderboard2.csv`.

## 📊 Data Fields

Typical columns scraped:
- API Provider
- Model
- Context Window
- AI Index
- Price (USD/1M Tokens)
- Tokens/s
- Latency (s)
- (Image logo filename if available)

## 🧰 Dependencies

- `requests`
- `beautifulsoup4`
- `pandas`


## 📌 Notes

- This script targets the actual embedded leaderboard at `https://artificialanalysis.ai/embed/llm-performance-leaderboard` because the Hugging Face Space uses an iframe.
- Any images found in the table are captured by filename only, not downloaded.

---