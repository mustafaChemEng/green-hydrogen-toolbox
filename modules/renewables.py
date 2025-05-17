import streamlit as st

def run():
    st.header("🌞 Renewable Energy Simulation")

    st.markdown("Simulate green hydrogen production using solar, wind, or hybrid energy sources.")

    energy_type = st.selectbox("Select energy source", ["Solar", "Wind", "Hybrid"])
    available_energy = st.number_input("🔋 Available energy per day (kWh)", min_value=0.0, step=100.0)
    efficiency = st.slider("⚙️ Electrolyzer efficiency (%)", min_value=30, max_value=100, value=70)

    if st.button("Simulate Production"):
        effective_energy = available_energy * (efficiency / 100)
        hydrogen_kg = effective_energy / 33.33  # 1 kg H2 ≈ 33.33 kWh

        st.success(f"🚀 Estimated Hydrogen Production: {hydrogen_kg:.2f} kg/day")
        st.info("Assumes electrolyzer operates only on available daily energy input.")
