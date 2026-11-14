
import streamlit as st
import os

st.title("School Distribution")

st.markdown("""
### Objective 2 – School distribution

To examine the number and distribution of schools across states,
districts and school types from 2019 to 2023.
""")

st.markdown("---")

st.header("School Distribution Analysis")

st.write("""
This section examines the distribution of schools across
Malaysian states, districts and school types.
""")

st.info(
    "Note: The 2023 school data is dated 30 June 2023. "
    "Therefore, it represents a mid-year record rather than a full-year total."
)

# Locate chart folder
chart_folder = (
    "charts" if os.path.exists("charts")
    else "all_visualization_charts"
)

# Chart 1
st.subheader("1. Number of Schools by State in 2022")

image_path = os.path.join(
    chart_folder, "schools_by_state.png"
)

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error("Schools by state chart not found.")

# Chart 2
st.subheader("2. Top 10 Districts by Number of Schools in 2022")

image_path = os.path.join(
    chart_folder, "schools_by_district.png"
)

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error("Schools by district chart not found.")

# Chart 3
st.subheader("3. Number of Schools by Type (2019–2023)")

image_path = os.path.join(
    chart_folder, "schools_by_type.png"
)

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error("Schools by type chart not found.")

st.markdown("---")

st.caption("Scientific Visualization Assignment | Malaysia")

