# app.py (Dairy Survey Multilingual + CSV Download)

import streamlit as st
import pandas as pd
import datetime
import os

# Multilingual Translations
translations = {
    'English': {
        'Farmer Name': 'Farmer Name', 'Farmer Code': 'Farmer Code', 'Gender': 'Gender',
        'Select Gender': 'Select Gender', 'Male': 'Male', 'Female': 'Female',
        'Submit': 'Submit', 'Language': 'Language', 'Download CSV': 'Download CSV'
    },
    'Hindi': {
        'Farmer Name': 'किसान का नाम', 'Farmer Code': 'किसान कोड', 'Gender': 'लिंग',
        'Select Gender': 'लिंग चुनें', 'Male': 'पुरुष', 'Female': 'महिला',
        'Submit': 'जमा करें', 'Language': 'भाषा', 'Download CSV': 'सीएसवी डाउनलोड करें'
    },
    'Telugu': {
        'Farmer Name': 'రైతు పేరు', 'Farmer Code': 'రైతు కోడ్', 'Gender': 'లింగం',
        'Select Gender': 'లింగాన్ని ఎంచుకోండి', 'Male': 'పురుషుడు', 'Female': 'స్త్రీ',
        'Submit': 'సమర్పించండి', 'Language': 'భాష', 'Download CSV': 'CSV డౌన్లోడ్ చేయండి'
    },
    'Marathi': {
        'Farmer Name': 'शेतकऱ्याचे नाव', 'Farmer Code': 'शेतकरी कोड', 'Gender': 'लिंग',
        'Select Gender': 'लिंग निवडा', 'Male': 'पुरुष', 'Female': 'स्त्री',
        'Submit': 'सबमिट करा', 'Language': 'भाषा', 'Download CSV': 'CSV डाउनलोड करा'
    }
}

st.set_page_config(page_title="Dairy Survey", page_icon="🐄", layout="centered")

lang = st.selectbox("Select Language / भाषा / భాష / भाषा", ("English", "Hindi", "Telugu", "Marathi"))
labels = translations.get(lang, translations['English'])

st.title(labels['Farmer Name'] + " ✨ " + labels['Farmer Code'])

with st.form("survey_form"):
    farmer_name = st.text_input(labels['Farmer Name'])
    farmer_code = st.text_input(labels['Farmer Code'])
    gender = st.selectbox(labels['Gender'], (labels['Male'], labels['Female']))
    submit = st.form_submit_button(labels['Submit'])

if submit:
    now = datetime.datetime.now()
    data = {
        'Timestamp': [now.isoformat()],
        'Language': [lang],
        'Farmer Name': [farmer_name],
        'Farmer Code': [farmer_code],
        'Gender': [gender]
    }
    df = pd.DataFrame(data)

    if os.path.exists("survey_data.csv"):
        df.to_csv("survey_data.csv", mode='a', header=False, index=False, encoding='utf-8')
    else:
        df.to_csv("survey_data.csv", index=False, encoding='utf-8')

    st.success("✅ Survey Saved Successfully!")

# Show Download button if file exists
if os.path.exists("survey_data.csv"):
    with open("survey_data.csv", "rb") as f:
        st.download_button(
            label=labels['Download CSV'],
            data=f,
            file_name="survey_data.csv",
            mime="text/csv"
        )
