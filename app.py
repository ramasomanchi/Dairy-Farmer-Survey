# app.py

import streamlit as st
import pandas as pd
import os
import datetime

# -------------------------
# Translation dictionary
# -------------------------
translations = {
    'English': {
        'Farmer Name': 'Farmer Name',
        'Farmer Code': 'Farmer Code',
        'Gender': 'Gender',
        'Select Gender': 'Select Gender',
        'Male': 'Male',
        'Female': 'Female',
        'HPC/MCC Name': 'HPC/MCC Name',
        'HPC/MCC Code': 'HPC/MCC Code',
        'Type': 'Type',
        'Select Type': 'Select Type',
        'HPCC': 'HPCC',
        'MCC': 'MCC',
        'Number of Cows': 'Number of Cows',
        'No. of Cattle in Milk': 'No. of Cattle in Milk',
        'No. of Calves/Heifers': 'No. of Calves/Heifers',
        'No. of Desi Cows': 'No. of Desi Cows',
        'No. of Crossbreed Cows': 'No. of Crossbreed Cows',
        'No. of Buffalo': 'No. of Buffalo',
        'Milk Production (liters/day)': 'Milk Production (liters/day)',
        'Source of Water': 'Source of Water',
        'Submit': 'Submit',
    },
    'Hindi': {
        'Farmer Name': 'किसान का नाम',
        'Farmer Code': 'किसान कोड',
        'Gender': 'लिंग',
        'Select Gender': 'लिंग चुनें',
        'Male': 'पुरुष',
        'Female': 'महिला',
        'HPC/MCC Name': 'एचपीसी/एमसीसी नाम',
        'HPC/MCC Code': 'एचपीसी/एमसीसी कोड',
        'Type': 'प्रकार',
        'Select Type': 'प्रकार चुनें',
        'HPCC': 'एचपीसीसी',
        'MCC': 'एमसीसी',
        'Number of Cows': 'गायों की संख्या',
        'No. of Cattle in Milk': 'दूध वाली गायों की संख्या',
        'No. of Calves/Heifers': 'बछड़ों/हिफर्स की संख्या',
        'No. of Desi Cows': 'देसी गायों की संख्या',
        'No. of Crossbreed Cows': 'क्रॉसब्रीड गायों की संख्या',
        'No. of Buffalo': 'भैंसों की संख्या',
        'Milk Production (liters/day)': 'दूध उत्पादन (लीटर/दिन)',
        'Source of Water': 'पानी का स्रोत',
        'Submit': 'जमा करें',
    },
    'Telugu': {
        'Farmer Name': 'రైతు పేరు',
        'Farmer Code': 'రైతు కోడ్',
        'Gender': 'లింగం',
        'Select Gender': 'లింగం చయందించండి',
        'Male': 'పురుషుడు',
        'Female': 'స్త్రీ',
        'HPC/MCC Name': 'హ్పిసీ/ఎంసీసీ పేరు',
        'HPC/MCC Code': 'హ్పిసీ/ఎంసీసీ కోడ్',
        'Type': 'ప్రకారం',
        'Select Type': 'ప్రకారం చయందించండి',
        'HPCC': 'HPCC',
        'MCC': 'MCC',
        'Number of Cows': 'అవుల సంఖ్య',
        'No. of Cattle in Milk': 'పాలు లో ఉన్నతా జనాలు',
        'No. of Calves/Heifers': 'కారులు/హైఫర్స్ సంఖ్య',
        'No. of Desi Cows': 'దేసి అవుల సంఖ్య',
        'No. of Crossbreed Cows': 'క్రాస్బ్రీడ్ అవుల సంఖ్య',
        'No. of Buffalo': 'మేలకుల సంఖ్య',
        'Milk Production (liters/day)': 'పాలు ఉత్పాదనం (లీటర్లు/రోజు)',
        'Source of Water': 'నీటి తొట్టి',
        'Submit': 'సమర్పించండి',
    }
}

# -------------------------
# Streamlit App
# -------------------------
st.set_page_config(page_title="Dairy Survey Form", page_icon="🐮", layout="centered")

st.title("🐮 Dairy Farmer Survey")

lang = st.selectbox("Select Language", list(translations.keys()))
labels = translations.get(lang)

# Form
with st.form("survey_form"):
    farmer_name = st.text_input(labels['Farmer Name'])
    farmer_code = st.text_input(labels['Farmer Code'])
    gender = st.selectbox(labels['Gender'], [labels['Male'], labels['Female']])
    hpc_name = st.text_input(labels['HPC/MCC Name'])
    hpc_code = st.text_input(labels['HPC/MCC Code'])
    farmer_type = st.selectbox(labels['Type'], [labels['HPCC'], labels['MCC']])
    cows = st.number_input(labels['Number of Cows'], min_value=0)
    cattle_milk = st.number_input(labels['No. of Cattle in Milk'], min_value=0)
    calves = st.number_input(labels['No. of Calves/Heifers'], min_value=0)
    desi_cows = st.number_input(labels['No. of Desi Cows'], min_value=0)
    crossbreed_cows = st.number_input(labels['No. of Crossbreed Cows'], min_value=0)
    buffaloes = st.number_input(labels['No. of Buffalo'], min_value=0)
    milk_production = st.number_input(labels['Milk Production (liters/day)'], min_value=0)
    water_source = st.text_input(labels['Source of Water'])

    submit = st.form_submit_button(labels['Submit'])

# Save Submission
if submit:
    if not os.path.exists("survey_responses"):
        os.makedirs("survey_responses")

    new_data = {
        'Timestamp': datetime.datetime.now().isoformat(),
        'Language': lang,
        'Farmer Name': farmer_name,
        'Farmer Code': farmer_code,
        'Gender': gender,
        'HPC/MCC Name': hpc_name,
        'HPC/MCC Code': hpc_code,
        'Type': farmer_type,
        'Number of Cows': cows,
        'No. of Cattle in Milk': cattle_milk,
        'No. of Calves/Heifers': calves,
        'No. of Desi Cows': desi_cows,
        'No. of Crossbreed Cows': crossbreed_cows,
        'No. of Buffalo': buffaloes,
        'Milk Production (liters/day)': milk_production,
        'Source of Water': water_source
    }

    df = pd.DataFrame([new_data])

    csv_path = "survey_responses/responses.csv"
    if os.path.exists(csv_path):
        df.to_csv(csv_path, mode='a', index=False, header=False)
    else:
        df.to_csv(csv_path, index=False)

    st.success("✅ Survey response saved successfully!")

# View and Download past submissions
if os.path.exists("survey_responses/responses.csv"):
    st.subheader("📅 Past Submissions")
    data = pd.read_csv("survey_responses/responses.csv")
    st.dataframe(data)

    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="🔖 Download All Submissions",
        data=csv,
        file_name='survey_submissions.csv',
        mime='text/csv'
    )
