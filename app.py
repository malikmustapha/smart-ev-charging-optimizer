import streamlit as st
import pandas as pd
from optimizer import optimize_charging_schedule

st.title("⚡ Smart EV Charging Optimizer")

df = pd.read_csv('data/hourly_prices.csv', parse_dates=['datetime'])

st.line_chart(df.set_index('datetime')['price'])

# User input
st.sidebar.header("⚙️ Charging Settings")
deadline = st.sidebar.slider('Finish charging by hour (0-23):', 0, 23, 8)
needed_kwh = st.sidebar.number_input('How many kWh to charge?', min_value=1, value=30)
charger_rate = st.sidebar.number_input('Charger rate (kW):', min_value=1, value=7)

# Optimize
selected_hours, total_cost = optimize_charging_schedule(df, needed_kwh, charger_rate, deadline)
st.write("Selected hours shape:", selected_hours.shape)
st.write(selected_hours)

st.subheader("📌 Recommended Charging Hours")
st.write(selected_hours[['datetime', 'price']])

st.subheader("💰 Estimated Total Cost")
st.write(f"${total_cost:.2f}")
