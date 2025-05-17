import streamlit as st  
import numpy as np  
import pandas as pd  
import plotly.graph_objects as go

def run():  
    st.header("🌍 Renewable Energy Profile Simulation")

    st.markdown("Simulate solar and wind energy availability and estimate hydrogen production over 24 hours.")

    st.subheader("🔆 Solar Panel Parameters")
    solar_power = st.number_input("Peak Solar Power Output (kW)", min_value=0.0, value=100.0)
    solar_eff = st.slider("Solar Efficiency (%)", min_value=5, max_value=25, value=18)

    st.subheader("💨 Wind Turbine Parameters")
    wind_power = st.number_input("Peak Wind Power Output (kW)", min_value=0.0, value=50.0)
    wind_eff = st.slider("Wind Efficiency (%)", min_value=10, max_value=60, value=35)

    st.subheader("⚡ Hourly Simulation")

    hours = np.arange(0, 24)
    # Dummy solar profile: bell curve centered around noon
    solar_profile = np.maximum(0, np.sin((hours - 6) * np.pi / 12)) * solar_power * (solar_eff / 100)
    # Dummy wind profile: random but consistent
    np.random.seed(42)
    wind_profile = wind_power * (wind_eff / 100) * (0.6 + 0.4 * np.random.rand(24))

    total_energy = solar_profile + wind_profile
    hydrogen_kg = total_energy * 0.05  # Estimate: 1 kWh ≈ 0.05 kg H₂

    df = pd.DataFrame({
        "Hour": hours,
        "Solar (kWh)": solar_profile,
        "Wind (kWh)": wind_profile,
        "Total Energy (kWh)": total_energy,
        "H₂ Produced (kg)": hydrogen_kg
    })

    # Visualization
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hours, y=solar_profile, mode='lines+markers', name='Solar'))
    fig.add_trace(go.Scatter(x=hours, y=wind_profile, mode='lines+markers', name='Wind'))
    fig.add_trace(go.Scatter(x=hours, y=hydrogen_kg, mode='lines+markers', name='H₂ Produced'))

    fig.update_layout(title='Hourly Renewable Energy and H₂ Production', xaxis_title='Hour', yaxis_title='kWh / kg')

    st.plotly_chart(fig)
    st.dataframe(df)
