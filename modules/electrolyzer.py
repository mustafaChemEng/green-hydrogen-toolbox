import streamlit as st

def run():
    st.header("⚡ Electrolyzer Energy & Sizing Tool")

    h2_kg = st.number_input("🎯 Hydrogen production goal (kg/day)", min_value=1.0, step=1.0)
    efficiency = st.slider("⚙️ Electrolyzer efficiency (%)", min_value=30, max_value=100, value=70)
    hours = st.slider("⏱️ Operating hours per day", 1, 24, 24)

    if st.button("Estimate Energy Usage"):
        h2_energy_kwh = 33.33 * h2_kg
        required_energy = h2_energy_kwh / (efficiency / 100)
        required_power = required_energy / hours

        st.success(f"🔋 Total Daily Energy Required: {required_energy:.2f} kWh/day")
        st.success(f"⚡ Required Power Input: {required_power:.2f} kW")
        st.info("Hydrogen energy value assumed: 33.33 kWh/kg")
