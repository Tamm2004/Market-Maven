# 📈 Market Maven

Market Maven is a **stock market analysis web application** built with **Django** and **Python**. It lets you explore stock data, visualize trends, and gain insights from historical CSV datasets. The project combines backend logic with frontend templates to present static and interactive analyses.

## 🧾 Project Overview

Market Maven includes:

- 📊 Historical stock price data (`.csv` files) for major companies  
- 🐍 Django web app to serve data and display visualizations  
- 🧠 Python analysis logic for processing stock information  
- 📁 Templates & static files for clean UI rendering  
- 🗃️ SQLite database used for quick prototyping and local storage :contentReference[oaicite:1]{index=1}

---

## 🚀 Features

- 📈 View and compare historical stock prices
- 🔍 Load and display multiple company stocks
- 🧮 Backend logic using Pandas and Python for analysis
- 🖼️ Frontend templates with charts and tables
- 🧠 Designed to be extendable with more analytics

---

## 📦 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python     | Backend programming |
| Django     | Web framework |
| SQLite     | Local database |
| HTML/CSS   | Frontend UI |
| CSV        | Stock data format |

---

## 📁 Project Structure
```
Market-Maven/
├── StockAnalysis/ # Analysis Python scripts (if any)
├── templates/ # HTML templates
├── statics/ # CSS, JS, media
├── media/ # Uploaded or generated media files
├── *.csv # Stock dataset files
├── db.sqlite3 # Local database
├── manage.py # Django management script
└── ...
```

---

## 🧠 How It Works

1. Load the Django app using `manage.py`
2. Use CSV files to populate or visualize stock statistics
3. Render insights via Django views & templates

---

## 📥 Installation

### Prerequisites
Make sure you have:

- Python 3.x
- Django
- pandas, matplotlib (or other libs you use)

---

### Setup Steps

```bash
# 1) Clone the repository
git clone https://github.com/Tamm2004/Market-Maven.git

# 2) Navigate to project folder
cd Market-Maven

# 3) Create virtual environment (optional)
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# 4) Install dependencies
pip install -r requirements.txt

# 5) Run database migrations
python manage.py migrate

# 6) Start development server
python manage.py runserver
