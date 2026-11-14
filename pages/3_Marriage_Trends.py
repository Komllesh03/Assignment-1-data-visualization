
import streamlit as st
import os

st.title("Marriage Trends")

st.markdown("""
### Objective 3 – Marriage trends

To analyse how marriages changed across states and by sex from
2019 to 2023, and to explore how they relate to household income.
""")

st.markdown("---")

st.header("Marriage Trends Analysis")

st.write("""
This section explores marriage trends across Malaysian states
and compares marriage rates between females and males.
It also examines the relationship between household income
and marriage rates.
""")

st.info(
    "Note: The marriage and household income comparison uses "
    "2019, 2020 and 2022 because these are the overlapping years "
    "available in both datasets."
)

# Locate chart folder
chart_folder = (
    "charts" if os.path.exists("charts")
    else "all_visualization_charts"
)

# Chart 1
st.subheader("1. Marriage Trends by Sex (2019–2023)")

image_path = os.path.join(
    chart_folder, "marriage_trends_by_sex.png"
)

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error("Marriage trends chart not found.")

st.write("""
Both female and male marriage rates peaked in 2021
and reached their lowest levels in 2023.
The average female marriage rate was higher than the
average male marriage rate in every year.
""")

# Chart 2
st.subheader("2. Marriage Rates by State and Sex in 2023")

image_path = os.path.join(
    chart_folder, "marriage_by_state_and_sex.png"
)

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error("Marriage by state and sex chart not found.")

# Chart 3
st.subheader("3. Relationship Between Household Income and Marriage Rates")

image_path = os.path.join(
    chart_folder, "income_and_marriage_relationship.png"
)

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error("Income and marriage relationship chart not found.")

st.write("""
The analysis shows a moderate negative association between
household income and marriage rates, with an overall correlation
of approximately -0.423.

This indicates that higher household income was associated
with lower marriage rates in the analysed data. However,
correlation does not prove causation.
""")

st.markdown("---")

st.caption("Scientific Visualization Assignment | Malaysia")
