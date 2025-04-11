
import streamlit as st

st.title("📏 Simple Unit Converter")

conversion_type = "Length"

# Length conversion function
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000
    }
    return value * (length_units[to_unit] / length_units[from_unit])



units = ["Meter", "Kilometer", "Centimeter", "Millimeter"]
from_unit = st.selectbox("Convert from:", units)
to_unit = st.selectbox("Convert to:", units)
value = st.number_input("Enter value:", min_value=0.0)


# Convert and display result

if st.button("Convert"):
    result = convert_length(value, from_unit, to_unit)
    st.success(f"Converted Value: {result:.3f} {to_unit}")
