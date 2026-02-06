import streamlit as st
import time

# App Title and Styling
st.set_page_config(page_title="Headphone QC", page_icon="🎧")
st.title("🎧 Headphone QC Tester")
st.info("Grading Tool for Mobiles & Accessories")

# Step 1: Device Info
st.subheader("Step 1: Connection Details")
brand = st.text_input("Enter Brand/Model", placeholder="e.g. Sony WH-1000XM4")

# Step 2: Power Status
st.subheader("Step 2: Power & Battery")
col1, col2 = st.columns(2)
with col1:
    charging = st.toggle("Charging Detected?")
with col2:
    battery = st.select_slider("Battery Level", options=["Low", "Medium", "High", "Full"])

# Steps 3, 4, & 5: Functional Tests
st.subheader("Functional Tests")
audio_test = st.checkbox("Step 3: L/R Audio (Passed)")
mic_test = st.checkbox("Step 4: Mic Quality (Passed)")
button_test = st.checkbox("Step 5: Physical Buttons (Passed)")

# Step 6: Final Grading Result
st.divider()
if st.button("GET FINAL GRADE", use_container_width=True):
    if brand and audio_test and mic_test and button_test and charging:
        st.balloons()
        st.success(f"GRADE: PASSED \n\n {brand} is ready for resale.")
    else:
        st.error(f"GRADE: DEFECT \n\n {brand} failed one or more requirements.")