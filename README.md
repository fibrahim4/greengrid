# 🌱 GreenGrid
A data dashboard that tracks renewable energy generation across the U.S., 
built for FusionHack 2026.

## The Problem
Most people have no idea how much clean energy their state actually produces. 
Data exists but it's buried in government databases that nobody looks at. 
GreenGrid makes that data visual and accessible.

## What GreenGrid Does
- National overview: see how much solar, wind, and hydro the U.S. generated in 2023
- State explorer: pick any state and see its renewable energy breakdown
- Trend tracker: see how clean energy has grown from 2015 to 2023
- Impact calculator: see how much CO₂ your state avoided by using renewables

## Tech Stack
- Python
- Streamlit
- Plotly
- Pandas
- EIA Open Data API

## How to Run
pip install -r requirements.txt
streamlit run app.py

## Data Source
U.S. Energy Information Administration (EIA) Open Data API.
Real government energy generation data by state and fuel type, 2015–2023.
