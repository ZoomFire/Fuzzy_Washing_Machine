import streamlit as st
import numpy as np
import pandas as pd
from fpdf import FPDF


# LOGIN SYSTEM
def login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.success("Login successful")
        else:
            st.error("Invalid username or password")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

# FUZZY LOGIC FUNCTIONS
def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

def weight_membership(w):
    return {
        "Light": triangular(w, 0, 2, 4),
        "Medium": triangular(w, 3, 5, 7),
        "Heavy": triangular(w, 6, 8, 10)
    }

def dirt_membership(d):
    return {
        "Low": triangular(d, 0, 2, 4),
        "Medium": triangular(d, 3, 5, 7),
        "High": triangular(d, 6, 8, 10)
    }

def fuzzy_controller(w, d):
    W = weight_membership(w)
    D = dirt_membership(d)

    slow = min(W["Light"], D["Low"])
    medium = max(
        min(W["Light"], D["High"]),
        min(W["Medium"], D["Low"])
    )
    fast = max(
        min(W["Medium"], D["High"]),
        min(W["Heavy"], D["Medium"]),
        min(W["Heavy"], D["High"])
    )

    speed = (slow * 400 + medium * 800 + fast * 1200) / (slow + medium + fast + 1e-6)

    explanation = (
        f"Light AND Low = {slow:.2f}\n"
        f"Medium rules = {medium:.2f}\n"
        f"Heavy rules = {fast:.2f}"
    )

    return speed, slow, medium, fast, explanation


# SAFE TEXT FOR PDF (IMPORTANT)
def safe_text(text):
    return text.encode("latin-1", "replace").decode("latin-1")

# STREAMLIT UI
st.set_page_config(page_title="Advanced Fuzzy Washing Machine", layout="wide")
st.title("🧺 Advanced Fuzzy Logic Washing Machine Controller")

tab1, tab2, tab3, tab4 = st.tabs([
    "🎛 Controller",
    "📥 CSV Upload",
    "🤖 Explainable AI",
    "📄 PDF Report"
])

# TAB 1: CONTROLLER
with tab1:
    st.subheader("Input Parameters")

    w = st.slider("Load Weight (kg)", 0.0, 10.0, 5.0, 0.1)
    d = st.slider("Dirt Level", 0.0, 10.0, 5.0, 0.1)

    if st.button("Compute Wash Speed"):
        speed, slow, medium, fast, explanation = fuzzy_controller(w, d)

        st.success(f"Final Wash Speed = {speed:.2f} RPM")

        st.write("### Rule Activation Values")
        st.write(f"Slow  : {slow:.2f}")
        st.write(f"Medium: {medium:.2f}")
        st.write(f"Fast  : {fast:.2f}")
# TAB 2: CSV UPLOAD

with tab2:
    st.subheader("Upload CSV File")
    st.write("CSV format: weight,dirt")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        speeds = []

        for _, row in df.iterrows():
            s, _, _, _, _ = fuzzy_controller(row["weight"], row["dirt"])
            speeds.append(round(s, 2))

        df["Wash Speed (RPM)"] = speeds
        st.dataframe(df)


# TAB 3: EXPLAINABLE AI
with tab3:
    st.subheader("Why this wash speed?")

    speed, slow, medium, fast, explanation = fuzzy_controller(w, d)

    st.text(explanation)

    if fast > medium:
        st.info("Decision leans towards FAST wash due to heavy load or high dirt.")
    elif medium > slow:
        st.info("Decision leans towards MEDIUM wash for balanced conditions.")
    else:
        st.info("Decision leans towards SLOW wash for light or delicate clothes.")


# TAB 4: PDF REPORT
with tab4:
    st.subheader("Generate PDF Project Report")

    if st.button("Generate PDF Report"):
        speed, slow, medium, fast, explanation = fuzzy_controller(w, d)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Fuzzy Logic Washing Machine Report", ln=1)

        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Load Weight: {w} kg", ln=1)
        pdf.cell(0, 10, f"Dirt Level: {d}", ln=1)
        pdf.cell(0, 10, f"Final Wash Speed: {speed:.2f} RPM", ln=1)

        pdf.ln(5)
        pdf.multi_cell(0, 10, safe_text("Rule Explanation:\n" + explanation))

        pdf.output("washing_machine_report.pdf")

        st.success("PDF generated successfully")
        st.download_button(
            "Download PDF",
            open("washing_machine_report.pdf", "rb"),
            file_name="washing_machine_report.pdf"
        )


# FOOTER
st.markdown("---")
st.caption("🚀 Advanced Fuzzy Logic Washing Machine")
