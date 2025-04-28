# app.py
import streamlit as st
import pandas as pd
import datetime
import os

# Setup
st.set_page_config(page_title="Dairy Farmer Survey 🐄", layout="centered")
DATA_FILE = "submissions/survey_data.csv"
os.makedirs("submissions", exist_ok=True)

# Translations
translations = {
    'English': {...},  # I'll insert full mapping below
    'Hindi': {...},
    'Telugu': {...},
    'Marathi': {...},
}

# Language Selection
lang = st.selectbox("🌐 Select Language / भाषा / భాష / भाषा", list(translations.keys()))
labels = translations.get(lang, translations['English'])

# Title
st.title(f"{labels['Farmer Name']} ✨ {labels['Farmer Code']}")

# Form
with st.form("survey_form", clear_on_submit=True):
    farmer_name = st.text_input(labels['Farmer Name'])
    farmer_code = st.text_input(labels['Farmer Code'])
    gender = st.selectbox(labels['Gender'], [labels['Male'], labels['Female']])
    hpc_name = st.text_input(labels['HPC/MCC Name'])
    hpc_code = st.text_input(labels['HPC/MCC Code'])
    farmer_type = st.selectbox(labels['Type'], [labels['HPCC'], labels['MCC']])
    num_cows = st.number_input(labels['Number of Cows'], min_value=0)
    cattle_milk = st.number_input(labels['No. of Cattle in Milk'], min_value=0)
    calves_heifers = st.number_input(labels['No. of Calves/Heifers'], min_value=0)
    desi_cows = st.number_input(labels['No. of Desi Cows'], min_value=0)
    cross_cows = st.number_input(labels['No. of Crossbreed Cows'], min_value=0)
    buffalos = st.number_input(labels['No. of Buffalo'], min_value=0)
    milk_prod = st.number_input(labels['Milk Production (liters/day)'], min_value=0)
    green_fodder = st.text_input(labels['Type of Green Fodder'])
    green_qty = st.number_input(labels['Quantity of Green Fodder (Kg/day)'], min_value=0)
    dry_fodder = st.text_input(labels['Type of Dry Fodder'])
    dry_qty = st.number_input(labels['Quantity of Dry Fodder (Kg/day)'], min_value=0)
    concentrate_brand = st.text_input(labels['Brand of Concentrate Feed'])
    concentrate_qty = st.number_input(labels['Quantity of Concentrate Feed (Kg/day)'], min_value=0)
    mineral_brand = st.text_input(labels['Brand of Mineral Mixture'])
    mineral_qty = st.number_input(labels['Quantity of Mineral Mixture (gm/day)'], min_value=0)
    silage_source_price = st.text_input(labels['Source and Price of Silage'])
    silage_qty = st.number_input(labels['Quantity of Silage (Kg/day)'], min_value=0)
    water_source = st.text_input(labels['Source of Water'])

    submitted = st.form_submit_button(labels['Submit'])

# Save Data
if submitted:
    submission = {
        'Timestamp': datetime.datetime.now().isoformat(),
        'Language': lang,
        'Farmer Name': farmer_name,
        'Farmer Code': farmer_code,
        'Gender': gender,
        'HPC/MCC Name': hpc_name,
        'HPC/MCC Code': hpc_code,
        'Type': farmer_type,
        'Number of Cows': num_cows,
        'No. of Cattle in Milk': cattle_milk,
        'No. of Calves/Heifers': calves_heifers,
        'No. of Desi Cows': desi_cows,
        'No. of Crossbreed Cows': cross_cows,
        'No. of Buffalo': buffalos,
        'Milk Production (liters/day)': milk_prod,
        'Type of Green Fodder': green_fodder,
        'Quantity of Green Fodder (Kg/day)': green_qty,
        'Type of Dry Fodder': dry_fodder,
        'Quantity of Dry Fodder (Kg/day)': dry_qty,
        'Brand of Concentrate Feed': concentrate_brand,
        'Quantity of Concentrate Feed (Kg/day)': concentrate_qty,
        'Brand of Mineral Mixture': mineral_brand,
        'Quantity of Mineral Mixture (gm/day)': mineral_qty,
        'Source and Price of Silage': silage_source_price,
        'Quantity of Silage (Kg/day)': silage_qty,
        'Source of Water': water_source,
    }
    df = pd.DataFrame([submission])
    if os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, mode='a', header=False, index=False, encoding='utf-8')
    else:
        df.to_csv(DATA_FILE, index=False, encoding='utf-8')
    st.success("✅ Survey submitted successfully!")

# View Past Submissions
if st.button("📂 View Past Submissions"):
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE, encoding='utf-8')
        st.dataframe(df)
    else:
        st.info("No submissions yet.")

# Download Past Submissions
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "rb") as f:
        st.download_button(
            label="📥 Download Submissions CSV",
            data=f,
            file_name="survey_data.csv",
            mime="text/csv"
        )
