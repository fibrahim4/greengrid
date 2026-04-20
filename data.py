import requests
import pandas as pd

API_KEY = "lnM87kXn1YRnfGayHs5elYvbadpeRcjcXTV403Cx"

url = f"https://api.eia.gov/v2/electricity/electric-power-operational-data/data/?api_key={API_KEY}&frequency=annual&data[0]=generation&facets[fueltypeid][]=SUN&facets[fueltypeid][]=WND&facets[fueltypeid][]=HYC&facets[sectorid][]=99&start=2015&end=2023&sort[0][column]=period&sort[0][direction]=desc&length=500"

response = requests.get(url)
raw = response.json()

df = pd.DataFrame(raw["response"]["data"])

df = df[['period', 'location', 'stateDescription', 'fueltypeid', 'fuelTypeDescription', 'generation']]
df.columns = ['year', 'state_code', 'state_name', 'fuel_id', 'fuel_type', 'generation_mwh']
df['generation_mwh'] = pd.to_numeric(df['generation_mwh'], errors='coerce')
df = df.dropna()
df['year'] = df['year'].astype(int)

def get_data():
    return df