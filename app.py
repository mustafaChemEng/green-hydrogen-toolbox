import streamlit as st
import os
import sys

from modules import water_cost
from modules import hydrogen_tank
from modules import renewable_energy
from modules import electrolyzer

st.set_page_config(page_title="Green Hydrogen Toolbox", layout="wide")

# Optional Debug Info
#st.write("Python path:", sys.path)
#st.write("Modules folder exists:", os.path.isdir("modules"))
#st.write("Files in modules folder:", os.listdir("modules") if os.path.isdir("modules") else "No modules folder found")

st.title("🌱 Green Hydrogen Engineering Toolbox")
st.markdown("Empowering sustainable hydrogen production with chemical engineering + Python.")

st.sidebar.title("🛠️ Green H₂ Toolbox")
page = st.sidebar.selectbox("📂 Choose Module", [
    "Renewable Energy Simulation",
    "Electrolyzer Estimator",
    "Water Cost Comparison",
    "Hydrogen Tank Design (Coming)"
])

if page == "Renewable Energy Simulation":
    renewable_energy.run()
elif page == "Electrolyzer Estimator":
    electrolyzer.run()
elif page == "Water Cost Comparison":
    water_cost.run()
elif page == "Hydrogen Tank Design (Coming)":
    hydrogen_tank.run()

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Developed with 💚 by Mustafa Ali Yahya Adam | Green Hydrogen Engineering Toolbox | 2025"
    "</div>",
    unsafe_allow_html=True,
)
