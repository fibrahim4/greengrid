import streamlit as st
import plotly.express as px
from data import get_data

st.set_page_config(page_title="GreenGrid", page_icon="🌱")

st.title("🌱 GreenGrid")
st.caption("U.S. Renewable Energy Dashboard")

df = get_data()

# --- SCREEN 1: National Overview ---
st.subheader("U.S. Renewable Energy Generation by Source (2023)")

national = df[(df['state_code'] == '90') & (df['year'] == 2023)]
national_grouped = national.groupby('fuel_type')['generation_mwh'].sum().reset_index()

fig1 = px.bar(
    national_grouped,
    x='fuel_type',
    y='generation_mwh',
    color='fuel_type',
    labels={'fuel_type': 'Energy Source', 'generation_mwh': 'Generation (thousand MWh)'},
    color_discrete_sequence=['#2ecc71', '#3498db', '#1abc9c']
)

st.plotly_chart(fig1, use_container_width=True)

# --- SCREEN 2: State Explorer ---
st.subheader("Explore by State")

states = df[df['state_code'] != '90']['state_name'].unique()
selected_state = st.selectbox("Pick a state:", sorted(states))

state_df = df[(df['state_name'] == selected_state) & (df['year'] == 2023)]
state_grouped = state_df.groupby('fuel_type')['generation_mwh'].sum().reset_index()

fig2 = px.pie(
    state_grouped,
    names='fuel_type',
    values='generation_mwh',
    color_discrete_sequence=['#2ecc71', '#3498db', '#1abc9c']
)

st.plotly_chart(fig2, use_container_width=True)

# --- SCREEN 3: Trend Over Time ---
st.subheader("U.S. Renewable Energy Trend (2015–2023)")

trend_df = df[df['state_code'] == '90']
trend_grouped = trend_df.groupby(['year', 'fuel_type'])['generation_mwh'].sum().reset_index()

fig3 = px.line(
    trend_grouped,
    x='year',
    y='generation_mwh',
    color='fuel_type',
    markers=True,
    labels={'year': 'Year', 'generation_mwh': 'Generation (thousand MWh)', 'fuel_type': 'Source'},
    color_discrete_sequence=['#2ecc71', '#3498db', '#1abc9c']
)

st.plotly_chart(fig3, use_container_width=True)

# --- SCREEN 4: Impact Calculator ---
st.subheader("💡 Your State's Impact")

impact_state = df[(df['state_name'] == selected_state) & (df['year'] == 2023)]
total_renewable = impact_state['generation_mwh'].sum()
co2_avoided = total_renewable * 0.386

st.metric(label=f"Renewables generated in {selected_state} (2023)", value=f"{total_renewable:,.0f} thousand MWh")
st.metric(label="Estimated CO₂ avoided vs. coal", value=f"{co2_avoided:,.0f} metric tons")
st.caption("CO₂ estimate based on EPA avg of 0.386 kg CO₂ per kWh avoided from coal displacement.")