import streamlit as st

def run():
    st.title("💧 Water Cost Comparison")

    st.markdown("""
    Compare the cost implications of using different water sources (freshwater vs desalinated) for hydrogen production.
    """)

    with st.expander("📘 Why Water Cost Matters"):
        st.markdown("""
        Water is a key input in electrolysis. While freshwater is often cheaper and more available, it may not be feasible in arid regions. Desalinated water can expand hydrogen production but increases costs and energy demand.
        """)

    st.subheader("🔢 Input Values")

    total_hydrogen_kg = st.number_input(
        "Total Hydrogen to be Produced (kg)", 
        min_value=0.0, 
        value=1000.0,
        help="Total hydrogen mass planned for production"
    )

    water_per_kg_h2 = st.slider(
        "Liters of Water per kg of H₂", 
        min_value=8.0, 
        max_value=12.0, 
        value=9.0,
        help="Usually 9 liters of water per kg of hydrogen"
    )

    cost_freshwater_per_m3 = st.number_input(
        "Freshwater Cost (USD/m³)", 
        min_value=0.0, 
        value=0.5
    )

    cost_desal_per_m3 = st.number_input(
        "Desalinated Water Cost (USD/m³)", 
        min_value=0.0, 
        value=1.5
    )

    # Calculations
    total_water_liters = total_hydrogen_kg * water_per_kg_h2
    total_water_m3 = total_water_liters / 1000

    total_cost_fresh = total_water_m3 * cost_freshwater_per_m3
    total_cost_desal = total_water_m3 * cost_desal_per_m3

    st.divider()
    st.subheader("📊 Cost Comparison")

    st.metric("Total Water Needed (m³)", f"{total_water_m3:.2f}")
    st.metric("💧 Freshwater Cost (USD)", f"${total_cost_fresh:,.2f}")
    st.metric("🌊 Desalinated Water Cost (USD)", f"${total_cost_desal:,.2f}")

    st.success("✅ Comparison complete. Choose the most cost-effective water source for your site.")
