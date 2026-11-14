
import streamlit as st
import os

st.title("Household Income Trends")

st.markdown("""
### Objective 1 – Household income trends

To visualise how household income changed across Malaysian states
between 2019 and 2022, and to show where it is highest and lowest.
""")

st.markdown("---")

st.header("Household Income Analysis")

st.write("""
This section explores the changes in mean household income
across 16 Malaysian states using data from 2019, 2020 and 2022.
""")

st.info(
    "Note: The dataset does not contain an observation for 2021. "
    "Therefore, the analysis uses 2019, 2020 and 2022."
)

# Locate chart folder
chart_folder = (
    "charts" if os.path.exists("charts")
    else "all_visualization_charts"
)

# Chart 1
st.subheader("1. Household Income Trends by State")

image_path = os.path.join(
    chart_folder, "income_trends_by_state.png"
)

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error("Household income trends chart not found.")

# Chart 2
st.subheader("2. Household Income Comparison in 2022")

image_path = os.path.join(
    chart_folder, "income_comparison_2022.png"
)

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error("Household income comparison chart not found.")

st.write("""
In 2022, W.P. Putrajaya recorded the highest mean household
income at RM13,473, while Kelantan recorded the lowest at RM4,885.
""")

# Chart 3
st.subheader("3. Household Income Heatmap")

image_path = os.path.join(
    chart_folder, "income_heatmap.png"
)

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error("Household income heatmap not found.")

st.markdown("---")

st.caption("Scientific Visualization Assignment | Malaysia")
