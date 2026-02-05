<p align="center">
  <a href="https://www.airbnb.com" target="_blank">
    <img src="Airbnb_Logo_Bélo.svg.png" width="250" alt="Airbnb Logo">
  </a>
</p>

<h1 align="center">U.S. Airbnb Analysis (2020 & 2023)</h1>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.7%2B-blue.svg" alt="Python">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Last%20Updated-2023-blueviolet.svg" alt="Last Updated">
  </a>
</p>

Exploratory data analysis and comparative insights on U.S. Airbnb listings using 2020 and 2023 snapshots. This project examines pricing behavior, regional variation, room-type trends, and market shifts over time through statistical analysis, visualization, and preliminary modeling.

---

## Project Overview
Since its launch in 2008, Airbnb has transformed the hospitality industry by enabling flexible, peer-to-peer accommodation options. This project analyzes U.S. Airbnb listings across two time periods (2020 and 2023) to identify pricing patterns, regional dynamics, and structural changes in the short-term rental market.

The analysis emphasizes reproducible EDA, interpretable visualizations, and modeling readiness for price prediction tasks.

---

## Data Sources
The datasets are compiled from publicly available listings provided by **Inside Airbnb**.

- Original compilation: October 20, 2020  
- Updated compilation: April 14, 2023  

---

## Dataset Files
- `AB_US_2020.csv` — loaded as `air2020`
- `AB_US_2023.csv` — loaded as `air2023`

---

## Dataset Features
Listing-level attributes include:
- Host and listing identifiers
- Listing title
- Latitude and longitude
- Neighborhood and city
- Price
- Room type
- Minimum nights
- Review counts and frequency
- Availability
- Host listing counts  

*(Exact column names may vary slightly by dataset version.)*

---

## Key Questions
- How do listing prices vary by region, city, and room type?
- How has Airbnb’s U.S. market composition changed between 2020 and 2023?
- Can listing attributes be used to predict price or popularity?
- What geographic or structural patterns emerge from the data?
- Can textual and numeric features inform better listing recommendations?

---

## Analysis Scope
The notebook includes:
- Data ingestion and cleaning
- Summary statistics and missing-value analysis
- Correlation analysis
- Outlier detection and removal
- KDE-based price distribution analysis
- City- and state-level aggregations
- Geographic visualization (Folium, choropleths)
- Cross-year comparisons (2020 vs 2023)
- Preliminary machine learning setup using scikit-learn

---

## Requirements
- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- plotly / plotly.express
- scikit-learn
- folium (for interactive maps)
- Jupyter Notebook or JupyterLab

---

## Installation
```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn folium
```
---

## Streamlit Dashboard
This repository also includes a **Streamlit application** that can be run locally to explore the datasets interactively. The dashboard supports:

- Switching between **2020** and **2023** listing snapshots  
- Filtering by **city**, **room type**, and **price range**  
- Quick KPI metrics (total listings, average/median price, reviews per month)  
- Interactive Plotly visualizations (histograms, bar charts)  
- A geographic map view using latitude/longitude  
- A raw data table for reviewing filtered records  

**Files:**
- `app.py` (Streamlit dashboard)
- `airbnb.png` (dashboard header image)

**Run locally:**
```bash
pip install streamlit pandas plotly
streamlit run app.py
```
## Author
**Nadia (Ncashy)**  
Data Analytics & Data Science  
GitHub Portfolio Project


