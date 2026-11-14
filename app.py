
import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Malaysia Data Visualization",
    page_icon="🇲🇾",
    layout="wide"
)

st.title("Malaysia Data Visualization")
st.subheader("An Exploration of Malaysian Household Income, School Distribution, and Marriage Trends")

st.markdown("---")

st.header("Project Introduction")

st.write("""
This project explores three important aspects of Malaysia:
household income, school distribution, and marriage trends.

Using data visualization techniques, the project aims to identify
patterns, compare differences across Malaysian states, and understand
the relationships between the selected datasets.
""")

st.markdown("---")

st.header("Research Objectives")

st.subheader("Objective 1 – Household income trends")
st.write("""
To visualise how household income changed across Malaysian states
between 2019 and 2022, and to show where it is highest and lowest.
""")

st.subheader("Objective 2 – School distribution")
st.write("""
To examine the number and distribution of schools across states,
districts and school types from 2019 to 2023.
""")

st.subheader("Objective 3 – Marriage trends")
st.write("""
To analyse how marriages changed across states and by sex from
2019 to 2023, and to explore how they relate to household income.
""")

st.markdown("---")

st.header("Dataset Overview")

@st.cache_data
def load_data():
    def find_file(filename):
        for path in [
            filename,
            os.path.join("data", filename)
        ]:
            if os.path.exists(path):
                return path

        raise FileNotFoundError(
            f"Dataset not found: {filename}"
        )

    income = pd.read_csv(
        find_file("hh_income_state (1).csv")
    )

    marriages = pd.read_csv(
        find_file("marriages_state (1).csv")
    )

    schools = pd.read_csv(
        find_file("schools_district (1).csv")
    )

    return income, marriages, schools


try:
    income, marriages, schools = load_data()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Household Income Records",
            value=f"{len(income):,}"
        )

    with col2:
        st.metric(
            label="Marriage Records",
            value=f"{len(marriages):,}"
        )

    with col3:
        st.metric(
            label="School Records",
            value=f"{len(schools):,}"
        )

    st.success("All three datasets loaded successfully.")

except FileNotFoundError as error:
    st.error(str(error))

st.markdown("---")

st.header("Explore the Visualizations")

st.write("""
Use the navigation menu on the left side of this application
to explore the three visualization sections:

1. Household Income Trends
2. School Distribution
3. Marriage Trends
""")

st.info(
    "Select a page from the sidebar to begin exploring "
    "the visualizations."
)

st.markdown("---")

st.caption("Scientific Visualization Assignment | Malaysia")
