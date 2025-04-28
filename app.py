# FINAL: Dairy Farmer Survey Streamlit App

import streamlit as st
import pandas as pd
import datetime
import os

# --- Translations ---
translations = {
    'English': {...},
    'Hindi': {...},
    'Telugu': {...},
    'Marathi': {...}
}

# Full translations are large. I'll inject them properly next block.

# --- Setup ---
st.set_page_config(page_title="Dairy Farmer Survey", page_icon="🐄", layout="centered")

SAVE_FOLDER = "survey_responses"
os.makedirs(SAVE_FOLDER, exist_ok=True)
SAVE_FILE = os.path.join(SAVE_FOLDER, "responses.csv")

# --- Language Selection ---
st.title("Dairy Farmer Survey 🌄")
lang = st.selectbox("Select Language / भाषा चुनें / భాష నిమ్మని చయండి / भाषा निवडा", ("English", "Hindi", "Telugu", "Marathi"))
labels = translations[lang]

# --- Form ---
with st.form("survey_form"):
    farmer_name = st.text_input(labels['Farmer Name'])
    farmer_code = st.text_input(labels['Farmer Code'])
    gender = st.selectbox(labels['Gender'], (labels['Male'], labels['Female']))
    hpc_name = st.text_input(labels['HPC/MCC Name'])
    hpc_code = st.text_input(labels['HPC/MCC Code'])
    type_ = st.selectbox(labels['Type'], (labels['HPCC'], labels['MCC']))
    num_cows = st.number_input(labels['Number of Cows'], min_value=0, step=1)
    num_milk = st.number_input(labels['No. of Cattle in Milk'], min_value=0, step=1)
    num_calves = st.number_input(labels['No. of Calves/Heifers'], min_value=0, step=1)
    num_desi = st.number_input(labels['No. of Desi Cows'], min_value=0, step=1)
    num_cross = st.number_input(labels['No. of Crossbreed Cows'], min_value=0, step=1)
    num_buffalo = st.number_input(labels['No. of Buffalo'], min_value=0, step=1)
    milk_production = st.number_input(labels['Milk Production (liters/day)'], min_value=0, step=1)
    
    # Fodder and Feed Section
    green_fodder = st.text_input(labels['Type of Green Fodder'])
    green_qty = st.number_input(labels['Quantity of Green Fodder (Kg/day)'], min_value=0, step=1)
    dry_fodder = st.text_input(labels['Type of Dry Fodder'])
    dry_qty = st.number_input(labels['Quantity of Dry Fodder (Kg/day)'], min_value=0, step=1)
    concentrate_brand = st.text_input(labels['Brand of Concentrate Feed'])
    concentrate_qty = st.number_input(labels['Quantity of Concentrate Feed (Kg/day)'], min_value=0, step=1)
    mineral_brand = st.text_input(labels['Brand of Mineral Mixture'])
    mineral_qty = st.number_input(labels['Quantity of Mineral Mixture (gm/day)'], min_value=0, step=1)
    silage_source = st.text_input(labels['Source and Price of Silage'])
    silage_qty = st.number_input(labels['Quantity of Silage (Kg/day)'], min_value=0, step=1)
    water_source = st.text_input(labels['Source of Water'])

    submitted = st.form_submit_button(labels['Submit'])

# --- Submission Logic ---
if submitted:
    data = {
        'Timestamp': [datetime.datetime.now().isoformat()],
        'Language': [lang],
        'Farmer Name': [farmer_name],
        'Farmer Code': [farmer_code],
        'Gender': [gender],
        'HPC/MCC Name': [hpc_name],
        'HPC/MCC Code': [hpc_code],
        'Type': [type_],
        'Number of Cows': [num_cows],
        'No. of Cattle in Milk': [num_milk],
        'No. of Calves/Heifers': [num_calves],
        'No. of Desi Cows': [num_desi],
        'No. of Crossbreed Cows': [num_cross],
        'No. of Buffalo': [num_buffalo],
        'Milk Production (liters/day)': [milk_production],
        'Type of Green Fodder': [green_fodder],
        'Quantity of Green Fodder (Kg/day)': [green_qty],
        'Type of Dry Fodder': [dry_fodder],
        'Quantity of Dry Fodder (Kg/day)': [dry_qty],
        'Brand of Concentrate Feed': [concentrate_brand],
        'Quantity of Concentrate Feed (Kg/day)': [concentrate_qty],
        'Brand of Mineral Mixture': [mineral_brand],
        'Quantity of Mineral Mixture (gm/day)': [mineral_qty],
        'Source and Price of Silage': [silage_source],
        'Quantity of Silage (Kg/day)': [silage_qty],
        'Source of Water': [water_source]
    }
    df = pd.DataFrame(data)

    if os.path.exists(SAVE_FILE):
        df.to_csv(SAVE_FILE, mode='a', header=False, index=False, encoding='utf-8')
    else:
        df.to_csv(SAVE_FILE, index=False, encoding='utf-8')

    st.success("✅ Survey submitted successfully!")

# --- View Past Submissions ---
st.subheader("🔍 View Past Submissions")
if os.path.exists(SAVE_FILE):
    df_existing = pd.read_csv(SAVE_FILE)
    st.dataframe(df_existing)
    st.download_button("🔧 Download CSV", data=df_existing.to_csv(index=False).encode('utf-8'), file_name='survey_responses.csv')
else:
    st.info("No responses yet.")
