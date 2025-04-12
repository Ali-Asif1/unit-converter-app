
import streamlit as st

st.title('"Welcome to Unit Converter"')


def main(value, from_unit, to_unit):
    length_units = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000
    }
    return value * (length_units[to_unit] / length_units[from_unit])



units = ["Meter", "Kilometer", "Centimeter", "Millimeter"]
value = float(st.number_input("Enter value:", min_value=0.0))
from_unit = st.selectbox("Convert from:", units)
to_unit = st.selectbox("Convert to:", units)


if st.button("Convert"):
    result = main(value, from_unit, to_unit)
    st.success(f"Converted Value: {result} {to_unit}")
