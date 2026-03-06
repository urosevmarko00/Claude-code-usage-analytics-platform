# LLM Usage Analytics Platform

This project implements a data pipeline and analytics dashboard for monitoring Large Language Model (LLM) usage based on telemetry logs.

The system ingests raw JSONL logs, processes them into a structured dataset, stores them in SQLite, and exposes analytics through a Streamlit dashboard.

---

# Architecture

Pipeline overview:
```
Raw telemetry logs
        ↓
    Log parsing
        ↓
Dataset normalization
        ↓
Processed dataset (CSV)
        ↓
  SQLite database
        ↓
SQL analytics queries
        ↓
Streamlit dashboard
```


---

# Project Structure
```
Claude_Code_Analytics_Platform

data/
raw/                # raw telemetry logs
processed/          # processed dataset
analytics.db        # SQLite database

dataset_generator/  # synthetic dataset generator

src/
ingestion/          # load JSONL logs
processing/         # parsing and dataset building
database/           # database connection and loading
analytics/          # SQL analytics queries
dashboard/          # Streamlit dashboard

notebooks/          # exploratory analysis
```

---

# Setup

Clone the repository.

Install dependencies:
```bash
pip install -r requirements.txt
```
---

# Data Pipeline

### 1. Generate or place telemetry logs in:
```
data/raw/
```
Required files:

```
employees.csv  
telemetry_logs.jsonl
```
To generate files:

```bash
python3 dataset_generator/generate_fake_data.py
```

For a realistic dataset, generate at least 100 engineers over a couple of months:

```bash
python3 dataset_generator/generate_fake_data.py --num-users 100 --num-sessions 5000 --days 60
```

### 2. Build processed dataset
```bash
python -m src.processing.build_dataset
```
### 3. Load dataset into SQLite
```bash
python -m src.database.load_to_db
```
This creates:

```
data/analytics.db
```
---

# Run Dashboard

```bash
python -m streamlit run src/dashboard/app.py
```


---

# Analytics Features

The dashboard provides insights into LLM usage:

User analytics
+ Top 10 most expensive users
+ Request counts per user

Usage trends
+ Token usage over time
+ Cost trends

Model analytics
+ Model usage distribution
+ Model efficiency (tokens per dollar)

Practice analytics
+ Token usage by engineering practice

Tool analytics
+ Tool call frequency
+ Success rate
+ Average result size

Operational metrics
+ Error counts
+ Hourly usage patterns

---

# Technologies

+ Python  
+ Pandas  
+ SQLite  
+ Streamlit  

---

# Dataset

Synthetic telemetry logs were generated to simulate LLM API usage, tool execution, and user activity across different engineering practices.

---

# Author

Marko Urošev