import streamlit as st
import math

def run():
    st.title("🛢️ Hydrogen Tank Design")

    st.markdown("""
    Estimate storage tank volume and basic design considerations for hydrogen under high pressure.
    """)

    with st.expander("📘 Background"):
        st.markdown("""
        Designing safe and efficient storage tanks for hydrogen requires understanding gas behavior under pressure. 
        We'll use the ideal gas law and basic cylindrical tank assumptions.
        """)

    st.subheader("🔢 Input Parameters")

    mass_kg = st.number_input("Hydrogen Mass to Store (kg)", min_value=0.0, value=10.0)
    temp_K = st.number_input("Storage Temperature (K)", min_value=0.0, value=298.0)
    pressure_bar = st.number_input("Storage Pressure (bar)", min_value=1.0, value=350.0)

    st.subheader("⚙️ Design Assumptions")
    length_m = st.number_input("Tank Length (m)", min_value=0.1, value=2.0)
    tank_shape = st.selectbox("Tank Shape", ["Cylindrical with hemispherical ends"])

    # Constants
    R = 8.314  # J/mol·K
    M_H2 = 2.016  # g/mol
    P = pressure_bar * 1e5  # convert bar to Pa

    # Convert mass to moles
    moles_H2 = (mass_kg * 1000) / M_H2

    # Ideal Gas Law: V = nRT/P
    V_m3 = (moles_H2 * R * temp_K) / P

    # Cylindrical tank volume equation: V = πr²L + (4/3)πr³ for two hemispheres
    # Solve for r numerically using a simple iteration
    def tank_volume(r):
        cylinder = math.pi * r**2 * length_m
        hemispheres = (4/3) * math.pi * r**3
        return cylinder + hemispheres

    radius_guess = 0.1
    for _ in range(1000):
        current_volume = tank_volume(radius_guess)
        if abs(current_volume - V_m3) < 1e-5:
            break
        radius_guess += 0.001

    diameter = radius_guess * 2

    st.divider()
    st.subheader("📐 Results")

    st.metric("Required Volume (m³)", f"{V_m3:.3f}")
    st.metric("Estimated Tank Radius (m)", f"{radius_guess:.3f}")
    st.metric("Estimated Tank Diameter (m)", f"{diameter:.3f}")

    st.success("✅ Tank dimension estimate complete. This is a basic engineering model. Consider safety margins and standards for actual implementation.")
