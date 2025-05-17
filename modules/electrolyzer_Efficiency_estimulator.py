import streamlit as st

def run():
    st.title("⚡ Electrolyzer Efficiency & Hydrogen Production")

    st.markdown("""
    Estimate the amount of hydrogen produced and the energy required based on your electrolyzer setup.
    """)

    with st.expander("📘 How It Works"):
        st.markdown("""
        Hydrogen is produced by splitting water via electrolysis using electrical energy.
        
        - The efficiency of this process depends on electrolyzer type.
        - The energy requirement to produce 1 kg of hydrogen ranges from 45–55 kWh depending on system design.
        """)

    st.subheader("🧪 Electrolyzer Selection")

    electrolyzer_type = st.selectbox(
        "Choose Electrolyzer Type",
        ["Alkaline", "PEM (Proton Exchange Membrane)", "SOEC (High Temp)"]
    )

    default_efficiencies = {
        "Alkaline": 65,
        "PEM (Proton Exchange Membrane)": 70,
        "SOEC (High Temp)": 80
    }

    efficiency = st.slider(
        "System Efficiency (%)", 
        min_value=40, 
        max_value=90, 
        value=default_efficiencies[electrolyzer_type],
        help="Select the realistic operating efficiency"
    )

    st.subheader("⚙️ Energy Input")

    total_energy_kWh = st.number_input(
        "Total Available Energy (kWh)", 
        min_value=0.0, 
        value=1000.0,
        help="How much electricity you have available for electrolysis"
    )

    # Calculate hydrogen produced
    energy_per_kg = 50 / (efficiency / 100)  # kWh needed per kg of H2
    hydrogen_produced = total_energy_kWh / energy_per_kg

    st.divider()
    st.subheader("📊 Results")

    st.metric("Estimated Hydrogen Produced (kg)", f"{hydrogen_produced:.2f}")
    st.metric("Energy Required per kg of H₂ (kWh)", f"{energy_per_kg:.2f}")
    st.success("✅ Calculation completed. Adjust values to compare different systems.")
