import os
import streamlit as st
from extractor import extract_bill_data
from excel_filler import fill_excel_template

st.set_page_config(
    page_title="SolarLoad AI",
    page_icon="☀️",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #1f2937;
}
.subtitle {
    font-size: 18px;
    color: #4b5563;
}
.success-box {
    background: #ecfdf5;
    padding: 16px;
    border-radius: 12px;
    color: #065f46;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">☀️ SolarLoad AI</div>', unsafe_allow_html=True)
st.markdown(
    "<div style='color: #6b7280; font-size:16px;'>Powered by Energybae</div>",
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Convert electricity bills into ready-to-use solar load Excel calculations.</div>',
    unsafe_allow_html=True
)

st.divider()

left, right = st.columns([1.1, 1])

with left:
    st.markdown("### 📤 Upload Bill")
    uploaded_bill = st.file_uploader(
        "Upload MSEDCL electricity bill image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_bill:
        st.image(uploaded_bill, caption="Uploaded Bill Preview", width="stretch")

with right:
    st.markdown("### ⚙️ How it works")
    st.markdown("""
    1. Upload electricity bill image  
    2. OCR extracts main bill details  
    3. Review/correct monthly units  
    4. Download ready solar analysis Excel  
    """)

    st.info("The app uses the company Excel template internally and preserves formulas.")

if uploaded_bill and st.button("Extract Data", width="stretch"):
    with st.spinner("Reading bill using OCR..."):
        st.session_state.bill_data = extract_bill_data(uploaded_bill)

if "bill_data" in st.session_state:
    st.divider()
    st.markdown("### 📋 Review Extracted Data")

    data = st.session_state.bill_data

    c1, c2, c3 = st.columns(3)

    with c1:
        consumer_name = st.text_input("Consumer Name", data.get("consumer_name", ""))
        consumer_number = st.text_input("Consumer Number", data.get("consumer_number", ""))

    with c2:
        units = st.text_input("Current Month Units", data.get("units_consumed", ""))
        bill_amount = st.text_input("Bill Amount", data.get("bill_amount", ""))

    with c3:
        sanctioned_load = st.text_input("Sanctioned Load", data.get("sanctioned_load_kw", ""))
        connection_type = st.text_input("Connection Type", data.get("connection_type", ""))

    fixed_charges = st.text_input("Fixed Charges", data.get("fixed_charges", "130"))

    st.markdown("### 📅 Monthly Units")
    st.caption("OCR extracts current month automatically. Review or enter historical monthly units before generating Excel.")

    default_monthly_units = data.get("monthly_units", {})

    months = [
        "February 2025",
        "March 2025",
        "April 2025",
        "May 2025",
        "June 2025",
        "July 2025",
        "August 2025",
        "September 2025",
        "October 2025",
        "November 2025",
        "December 2025",
        "January 2026"
    ]

    edited_monthly_units = {}
    cols = st.columns(3)

    for idx, month in enumerate(months):
        with cols[idx % 3]:
            default_value = default_monthly_units.get(month, "")
            value = st.text_input(month, value=str(default_value))

            if value.strip():
                edited_monthly_units[month] = value.strip()

    final_data = {
        "consumer_name": consumer_name,
        "consumer_number": consumer_number,
        "fixed_charges": fixed_charges,
        "sanctioned_load_kw": sanctioned_load,
        "connection_type": connection_type,
        "units_consumed": units,
        "bill_amount": bill_amount,
        "bill_month": "January 2026",
        "monthly_units": edited_monthly_units
    }

    with st.expander("View raw extracted JSON"):
        st.json(data)

    if st.button("Generate Excel", width="stretch"):
        template_path = "input/template.xlsx"

        if not os.path.exists(template_path):
            st.error("template.xlsx not found. Put it inside the input folder.")
        else:
            with st.spinner("Filling Excel template..."):
                output_path = fill_excel_template(template_path, final_data)

            st.markdown(
                '<div class="success-box">✅ Excel file generated successfully.</div>',
                unsafe_allow_html=True
            )

            with open(output_path, "rb") as file:
                st.download_button(
                    label="⬇️ Download Filled Excel",
                    data=file,
                    file_name="filled_output.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    width="stretch"
                )

st.markdown("---")
st.markdown(
    "<center style='color: gray; font-size:14px;'>Developed for Energybae • Internship Assignment</center>",
    unsafe_allow_html=True
)