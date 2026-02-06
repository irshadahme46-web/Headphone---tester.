import streamlit as st
import sys

# --- 1. SAFETY SHIELD (Stops "Bare Mode" Errors) ---
if not st.runtime.exists():
    from streamlit.web import cli as stcli
    sys.argv = ["streamlit", "run", sys.argv[0]]
    sys.exit(stcli.main())

# --- 2. APP SETUP ---
st.set_page_config(page_title="Headphone QC Pro", page_icon="🎧")
st.title("🎧 Headphone Automation Tester")

# --- 3. HARDWARE INFO ---
st.header("Step 1: Device Info")
brand = st.text_input("Brand/Model", value="Sony WH-1000XM4")
battery = st.slider("Battery Health %", 0, 100, 90)

# --- 4. STEREO & MIC TEST ---
st.header("Step 2: Functional Tests")
col1, col2 = st.columns(2)
with col1:
    st.write("Left Ear")
    st.audio("https://www.audiocheck.net/download.php?filename=AudioCheck.net_left.mp3")
with col2:
    st.write("Right Ear")
    st.audio("https://www.audiocheck.net/download.php?filename=AudioCheck.net_right.mp3")

st.write("---")
mic_test = st.audio_input("Test Microphone")
if mic_test:
    st.audio(mic_test)

# --- 5. FINAL GRADING ---
st.header("Step 3: Final Grade")
passed_audio = st.checkbox("Audio Quality Passed")
passed_mic = st.checkbox("Microphone Passed")

if st.button("GENERATE REPORT", use_container_width=True):
    if brand and passed_audio and passed_mic:
        st.balloons()
        st.success(f"PASSED: {brand} is ready!")
    else:
        st.error("FAILED: Requirements not met.")