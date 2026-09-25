import streamlit as st
from packaging_parser import calc_total_units, get_unit, parse_packaging
 
st.title("Process One Package")
 
raw_input = st.text_input(
    "Enter package data:",
    key="package_data",
    placeholder="12 eggs in 1 carton / 3 cartons in 1 box",
)
 
if raw_input:
    package = parse_packaging(raw_input)
    total = calc_total_units(package)
    unit = get_unit(package)
 
    for level in package:
        for name, quantity in level.items():
            st.info(f"{name} ➡️ {quantity}")
 
    st.success(f"Total 📦 Size: {total} {unit}")