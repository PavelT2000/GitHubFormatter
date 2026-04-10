# OnlinerCPUParser

A Python-based web scraper that aggregates CPU specifications, performance ratings, power consumption, and market pricing from **Technical City** and **Onliner.by**. The tool merges datasets, calculates a performance-to-price efficiency metric, and stores the results in a local SQLite database for quick querying and analysis.

## 📋 Features
- **Dual-Source Aggregation:** Scrapes technical specs from Technical City and pricing data from Onliner.by.
- **Intelligent Data Matching:** Aligns records across sources, automatically handling packaging variants (`(box)`, `(wof)`).
- **Efficiency Metric:** Calculates a `use` score (`rating / price`) to help identify cost-effective processors.
- **Local Database Storage:** Automatically creates and populates a SQLite database (`myDataBase.db`).
- **Automated Reporting:** Outputs summary statistics including total count, aggregate price, and average price in BYN.

## 🛠️ Prerequisites
- Python 3.8 or higher
- Active internet connection
- Required Python packages: `requests`, `beautifulsoup4`

## 📦 Installation
1. Clone or download the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage
Run the main script to execute the scraping pipeline, populate the database, and display summary statistics:
```bash
python app.py
```

**Expected Output:**
```
1/19 technical city
...
31/31 onliner
Таблица обновлена
Кол-во процессоров на данный момент: 450
Цена всех процессоров на данный момент: 125000.00 белорусских рублей
Средняя цена процессора: 277.78 белорусских рублей
```

## 📁 Project Structure
```
OnlinerCPUParser/
├── .aiignore          # AI/LLM exclusion rules
├── app.py             # Main script: scraping, processing, DB operations
├── myDataBase.db      # SQLite database (auto-generated on first run)
└── requirements.txt   # Python dependencies
```

## 🗄️ Database Schema
The script performs a **full refresh** on each execution, dropping and recreating the following table:

| Column     | Type   | Description                                  |
|------------|--------|----------------------------------------------|
| `producer` | TEXT   | CPU manufacturer (e.g., Intel, AMD)          |
| `model`    | TEXT   | Full processor model name                    |
| `price`    | REAL   | Current market price (BYN)                   |
| `rating`   | REAL   | Performance rating from Technical City       |
| `power`    | REAL   | TDP/Power consumption (Watts)                |
| `use`      | FLOAT  | Efficiency metric (`rating / price`)         |

> **Note:** The table is named `Proccessors` (as implemented in the source). This can be renamed in `app.py` if strict naming conventions are required.

## ⚙️ How It Works
1. **Technical City Scraping:** Iterates through pages 1–19, extracting CPU names, performance ratings, and power consumption from the HTML table structure.
2. **Onliner.by Scraping:** Iterates through pages 1–31, parsing embedded JSON-LD structured data to extract producer names and current prices.
3. **Data Normalization & Matching:** 
   - Strips `(box)` and `(wof)` suffixes from model names for accurate cross-referencing.
   - Merges records where normalized model names match across both datasets.
4. **Database Population:** Inserts matched records into SQLite, calculating the `use` metric dynamically during insertion.
5. **Reporting:** Queries the database to output aggregate statistics for all processors with a non-zero price.

## ⚠️ Limitations & Considerations
- **Pagination Ranges:** Page limits are hardcoded (`range(1, 20)` for Technical City, `range(1, 32)` for Onliner). Adjust these values in `app.py` as catalog sizes change.
- **Rate Limiting:** The script does not implement request delays. Frequent execution may trigger anti-bot protections. Consider adding `time.sleep()` between requests for production or scheduled use.
- **Data Volatility:** Web scraping relies on external site structures. Changes to HTML layouts or JSON-LD schemas may break the parser.
- **Currency:** All prices are scraped and reported in **Belarusian Rubles (BYN)**.
- **Table Naming:** The SQLite table contains a typo (`Proccessors`). Update the `CREATE TABLE` and query strings if strict naming conventions are required.
- **Version Control:** `myDataBase.db` is generated automatically and should be excluded from version control (e.g., add to `.gitignore`).

## 📜 Disclaimer
This tool is intended for **educational and personal use only**. Ensure compliance with the `robots.txt` policies and Terms of Service of the target websites before deploying, automating, or scaling this script.

## 📄 License
[Specify License, e.g., MIT]