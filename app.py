
import streamlit as st
import pandas as pd
import os

# Page configuration
st.set_page_config(
    page_title="Malaysia Data Visualization",
    page_icon="📊",
    layout="wide"
)

# Main title
st.title("Malaysia Data Visualization")
st.write(
    "An exploration of Malaysian household income, "
    "school distribution, and marriage trends."
)

st.markdown("---")

# Assignment objectives
st.header("Research Objectives")

st.subheader("Objective 1 – Household income trends")
st.write(
    "To visualise how household income changed across Malaysian "
    "states between 2019 and 2022, and to show where it is highest and lowest."
)

st.subheader("Objective 2 – School distribution")
st.write(
    "To examine the number and distribution of schools across states, "
    "districts and school types from 2019 to 2023."
)

st.subheader("Objective 3 – Marriage trends")
st.write(
    "To analyse how marriages changed across states and by sex from "
    "2019 to 2023, and to explore how they relate to household income."
)

st.markdown("---")

# Load datasets
@st.cache_data
def load_data():
    def find_file(filename):
        for path in [filename, os.path.join("data", filename)]:
            if os.path.exists(path):
                return path
        raise FileNotFoundError(filename)

    income = pd.read_csv(find_file("hh_income_state (1).csv"))
    marriages = pd.read_csv(find_file("marriages_state (1).csv"))
    schools = pd.read_csv(find_file("schools_district (1).csv"))

    return income, marriages, schools
try:
    income_df, marriages_df, schools_df = load_data()

    st.header("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Income Records", len(income_df))
    col2.metric("Marriage Records", len(marriages_df))
    col3.metric("School Records", len(schools_df))

except Exception as e:
    st.error(f"Unable to load datasets: {e}")

st.markdown("---")

# Visualizations
st.header("Data Visualizations")

chart_folder = "charts" if os.path.exists("charts") else "all_visualization_charts"

charts = {
    "Objective 1 – Household Income": [
        ("Household Income Trends by State",
         "income_trends_by_state.png"),
        ("Household Income Comparison in 2022",
         "income_comparison_2022.png"),
        ("Household Income Heatmap",
         "income_heatmap.png"),
        ("Income and Marriage Relationship",
         "income_and_marriage_relationship.png")
    ],
    "Objective 2 – School Distribution": [
        ("Schools by State",
         "schools_by_state.png"),
        ("Schools by District",
         "schools_by_district.png"),
        ("Schools by School Type",
         "schools_by_type.png")
    ],
    "Objective 3 – Marriage Trends": [
        ("Marriage Trends by Sex",
         "marriage_trends_by_sex.png"),
        ("Marriage by State and Sex",
         "marriage_by_state_and_sex.png")
    ]
}

for objective, chart_list in charts.items():
    st.subheader(objective)

    for title, filename in chart_list:
        image_path = os.path.join(chart_folder, filename)

        if os.path.exists(image_path):
            st.write(f"**{title}**")
            st.image(image_path, use_container_width=True)
        else:
            st.warning(f"Chart not found: {filename}")

st.markdown("---")

st.caption(
    "Scientific Visualization Assignment | Malaysia"
)
