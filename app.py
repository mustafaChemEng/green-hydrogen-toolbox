import streamlit as st
from modules import water_cost
from modules import hydrogen_tank

from modules import renewable_energy, electrolyzer  # only import modules that are ready
#st.sidebar.image("assets/images/logo.png", use_column_width=True)
#st.sidebar.markdown("### 👋 Welcome, Engineer!")
#st.sidebar.markdown("Explore sustainable hydrogen design tools 🌱")


st.set_page_config(page_title="Green Hydrogen Toolbox", layout="wide")
st.title("🌱 Green Hydrogen Engineering Toolbox")
st.markdown("Empowering sustainable hydrogen production with chemical engineering + Python.")

st.sidebar.title("🛠️Green H2 Toolbox")
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



#Copy Right
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Developed with 💚 by Mustafa Ali Yahya Adam | Green Hydrogen Engineering Toolbox | 2025"
    "</div>",
    unsafe_allow_html=True,
)
