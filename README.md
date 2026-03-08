# LLM Usage Analytics Platform

This project implements an **end-to-end analytics platform for Large Language Model (LLM) telemetry data**.

The system processes raw Claude Code telemetry logs, transforms them into a structured dataset, stores them in a database, and exposes insights through an interactive dashboard and API.

The goal is to extract **actionable insights about developer usage patterns, token consumption, and model efficiency**.

---

# Architecture

Pipeline overview:
```
Raw telemetry logs (JSONL)
    ↓
Log ingestion
    ↓
Event parsing & normalization
    ↓
Dataset cleaning & enrichment
    ↓
Processed dataset (CSV)
    ↓
SQLite storage
    ↓
SQL analytics layer
    ↓
Streamlit dashboard + FastAPI API
```


---

# Project Structure
```
Claude_Code_Analytics_Platform

data/
├── raw/ # Raw telemetry logs
├── processed/ # Cleaned dataset
└── analytics.db # SQLite analytics database

dataset_generator/
└── generate_fake_data.py # Synthetic telemetry generator

presentation/
└──LLM_Usage_Analytics_Insights.pdf # Insights presentation

src/
├── ingestion/ # JSONL loading
├── processing/ # log parsing & dataset building
├── database/ # SQLite connection and loading
├── analytics/ # analytics queries + forecasting
├── dashboard/ # Streamlit dashboard
├── api/ # FastAPI endpoints
└── utils/ # helper utilities

notebooks/
└── exploratory_analysis.ipynb
```

---

# Environment Requirements

The project requires a python environment that supports the following core libraries:

+ Pandas
+ Scikit-learn
+ Streamlit
+ FastAPI
+ Uvicorn

Recommended Pyton version:
```
Python 3.9 - 3.12
```

Python 3.13+ may cause compatibility issues with some versions of `scikit-learn`.

You can check your version:
```bash
python3 --version
```

## Virtual Environment Setup (Recommended)

### Windows
```bash
python3 -m venv venv
venv\Scripts\acivate
```

### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/acivate
```
---

## Windows Setup
When installing Python packages that contain compiled extensions (such as `scikit-learn`), Windows may require **Microsoft C++ Build Tools** .

If installation fails with errors related to `build tools`, install:

Microsoft C++ Build Tools

Download:

https://visualstudio.microsoft.com/visual-cpp-build-tools/

During installation select:

```
Desktop development with C++
```

After installation restart the terminal before installing dependencies.

---
## Linux Setup
Most Linux distributions already contain the required build tools.

If installation fails, install the standard Python build dependencies.

### Ubuntu / Debian
```bash
sudo apt update
sudo apt install python3-dev build-essential
```

---
# Setup

Clone the repository:
```bash
git clone <repo-url>
cd Claude_Code_Analytics_Platform
```

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
python3 -m src.processing.build_dataset
```
This step:
+ Parses telemetry logs
+ Normalizes nested JSON fields
+ Cleans numeric features
+ Joins user metadata
+ Produces:
```
data/processed/processed_events.csv
```

### 3. Load dataset into SQLite
```bash
python3 -m src.database.load_to_db
```
This creates:

```
data/analytics.db
```
---

# Run Dashboard

```bash
python3 -m streamlit run src/dashboard/app.py
```
---
# Dashboard Insights

The platform provides several analytics views:

## KPI Overview

High-level operational metrics:
+ Total requests
+ Total tokens
+ Total cost
+ Error rate

## User Analytics

+ Top 10 most expensive users
+ Requests per user
+ Token consumption per user

## Usage Trends

+ Token usage over time
+ Cost trends
+ Hourly activity patterns

## Model Analytics

+ Model usage distribution
+ Model efficiency (tokens per dollar)

## Engineering Practice Insights

+ Token usage by engineering practice
+ Cost distribution across teams

## Tool Usage
+ Tool invocation frequency
+ Tool success rate
+ Average tool output size

---

# Advanced Analytics

The platform includes several additional insights.

### Cost per Request
Measures LLM efficiency by calculating the average cost per API request.

### Token Usage Forecasting
A simple predictive model estimates future token usage trends using time-series regression.

### Model Efficiency
Evaluates models based on tokens generated per dollar spent.

---

# API Access

The analytics layer is also exposed through a REST API.

Example endpoints:

```
GET /users
GET /models
GET /usage/trend
GET /analytics/cost_per_request
```
Run the API:

```bash
uvicorn src.api.main:app --reload
```
---

# Performance Optimizations

To improve performance and reduce dataset size:

### Event Filtering

Only relevant telemetry events are stored:

```
claude_code.api_request
claude_code.tool_result
claude_code.api_error
```
This reduces dataset size by ~35%.

### Database Indexing

Indexes are created for frequently queried fields:

+ event_type
+ attr.user.email
+ attr.model

This significantly speeds up analytics queries.

---
# Exploratory Data Analysis

An exploratory notebook is included:

```
notebooks/exploratory_analysis.ipynb
```
It contains:
+ missing value analysis
+ event distribution
+ token usage exploration
+ dataset validation checks

---

# Technologies

Core technologies used in this project:
+ Python
+ Pandas
+ SQLite
+ Streamlit
+ FastAPI
+ Scikit-learn 

---

# Dataset

Synthetic telemetry logs were generated to simulate LLM API usage, tool execution, and user activity across different engineering practices.

---

# Author

Marko Urošev