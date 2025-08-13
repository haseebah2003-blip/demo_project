import streamlit as st
from data import sample_data
from rules import check_exempt, sepp_rules

st.set_page_config(page_title="Exempt Development Checker", layout="centered")

st.title(" NSW Exempt Development Checker")
st.write("Check if your shed or patio meets the **NSW SEPP 2008** Exempt Development criteria.")

st.header(" Select a Property")
property_choice = st.selectbox(
    "Choose a property:",
    [f"Property {p['property_id']} — {p['location']} — {p['lot_size']} m²" for p in sample_data]
)
selected_property = sample_data[int(property_choice.split()[1]) - 1]

st.header(" Proposed Structure Details")
structure_type = st.selectbox("Structure Type", ["shed", "patio"])
width = st.selectbox("Width (m)", [2, 3, 4, 5, 6], index=0)
length = st.selectbox("Length (m)", [2, 3, 4, 5, 6], index=0)
height = st.selectbox("Height (m)", [2.1, 2.4, 3.0, 3.5], index=0)

if st.button(" Run Assessment"):
    result = check_exempt(structure_type, width, length, height, selected_property['lot_size'])
    st.session_state.result = result  

if "result" in st.session_state:
    result = st.session_state.result
    if result["status"] == "success":
        st.success(result["result"])
    else:
        st.error(result["result"])

    st.write("**Explanation:**", result["explanation"])
    st.write("**Relevant SEPP Clauses:**")
    for clause in result["clauses"]:
        st.write(f"- {clause}")
