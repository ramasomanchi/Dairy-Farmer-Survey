# Updated Streamlit App

import streamlit as st
import pandas as pd
import datetime
import os

# Translations
dict_translations = {
    'English': {
        'Farmer Name': 'Farmer Name',
        'Farmer Code': 'Farmer Code',
        'Gender': 'Gender',
        'Select Gender': 'Select Gender',
        'Male': 'Male', 'Female': 'Female',
        'Submit': 'Submit', 'Language': 'Language',
        'Specific Questions': 'Specific Questions',
        'Green Fodder': 'Green Fodder',
        'Type of Green Fodder': 'Type of Green Fodder',
        'Quantity of Green Fodder': 'Quantity of Green Fodder (Kg/day)',
        'Dry Fodder': 'Dry Fodder',
        'Type of Dry Fodder': 'Type of Dry Fodder',
        'Quantity of Dry Fodder': 'Quantity of Dry Fodder (Kg/day)',
        'Concentrate Feed': 'Concentrate Feed',
        'Brand of Concentrate Feed': 'Brand of Concentrate Feed',
        'Quantity of Concentrate Feed': 'Quantity of Concentrate Feed (Kg/day)',
        'Mineral Mixture': 'Mineral Mixture',
        'Brand of Mineral Mixture': 'Brand of Mineral Mixture',
        'Quantity of Mineral Mixture': 'Quantity of Mineral Mixture (gms/day)',
        'Silage': 'Silage',
        'Source and Price of Silage': 'Source and Price of Silage',
        'Quantity of Silage': 'Quantity of Silage (Kg/day)',
        'Source of Water': 'Source of Water',
        'Yes': 'Yes', 'No': 'No'
    },
    'Hindi': {
        'Farmer Name': 'किसान का नाम',
        'Farmer Code': 'किसान कोड',
        'Gender': 'लिंग',
        'Select Gender': 'लिंग चुनें',
        'Male': 'पुरुष', 'Female': 'महिला',
        'Submit': 'जमा करें', 'Language': 'भाषा',
        'Specific Questions': 'विशेष प्रश्न',
        'Green Fodder': 'हरा चारा',
        'Type of Green Fodder': 'हरे चारे का प्रकार',
        'Quantity of Green Fodder': 'हरे चारे की मात्रा (Kg/day)',
        'Dry Fodder': 'सूखा चारा',
        'Type of Dry Fodder': 'सूखे चारे का प्रकार',
        'Quantity of Dry Fodder': 'सूखे चारे की मात्रा (Kg/day)',
        'Concentrate Feed': 'सांद्रित चारा',
        'Brand of Concentrate Feed': 'सांद्रित चारे का ब्रांड',
        'Quantity of Concentrate Feed': 'सांद्रित चारे की मात्रा (Kg/day)',
        'Mineral Mixture': 'खनिज मिश्रण',
        'Brand of Mineral Mixture': 'खनिज मिश्रण का ब्रांड',
        'Quantity of Mineral Mixture': 'खनिज मिश्रण की मात्रा (gms/day)',
        'Silage': 'साइलेज',
        'Source and Price of Silage': 'साइलेज का स्रोत और मूल्य',
        'Quantity of Silage': 'साइलेज की मात्रा (Kg/day)',
        'Source of Water': 'पानी का स्रोत',
        'Yes': 'हाँ', 'No': 'नही'
    }
}

st.set_page_config(page_title="Dairy Farmer Survey", layout="centered")

lang = st.selectbox("Select Language", list(dict_translations.keys()))
labels = dict_translations.get(lang, dict_translations['English'])

st.title(labels['Farmer Name'] + " ✨ " + labels['Farmer Code'])

with st.form("survey_form"):
    farmer_name = st.text_input(labels['Farmer Name'])
    farmer_code = st.text_input(labels['Farmer Code'])
    gender = st.selectbox(labels['Gender'], (labels['Male'], labels['Female']))

    st.subheader(labels['Specific Questions'])
    green_fodder = st.selectbox(labels['Green Fodder'], (labels['Yes'], labels['No']))
    type_green = st.text_input(labels['Type of Green Fodder'])
    qty_green = st.number_input(labels['Quantity of Green Fodder'], min_value=0)

    dry_fodder = st.selectbox(labels['Dry Fodder'], (labels['Yes'], labels['No']))
    type_dry = st.text_input(labels['Type of Dry Fodder'])
    qty_dry = st.number_input(labels['Quantity of Dry Fodder'], min_value=0)

    concentrate = st.selectbox(labels['Concentrate Feed'], (labels['Yes'], labels['No']))
    brand_concentrate = st.text_input(labels['Brand of Concentrate Feed'])
    qty_concentrate = st.number_input(labels['Quantity of Concentrate Feed'], min_value=0)

    mineral = st.selectbox(labels['Mineral Mixture'], (labels['Yes'], labels['No']))
    brand_mineral = st.text_input(labels['Brand of Mineral Mixture'])
    qty_mineral = st.number_input(labels['Quantity of Mineral Mixture'], min_value=0)

    silage = st.selectbox(labels['Silage'], (labels['Yes'], labels['No']))
    source_price = st.text_input(labels['Source and Price of Silage'])
    qty_silage = st.number_input(labels['Quantity of Silage'], min_value=0)

    water_source = st.text_input(labels['Source of Water'])

    submit = st.form_submit_button(labels['Submit'])

if submit:
    folder = 'survey_responses'
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, 'responses.csv')
    now = datetime.datetime.now()

    data = {
        'Timestamp': [now.isoformat()], 'Language': [lang],
        'Farmer Name': [farmer_name], 'Farmer Code': [farmer_code], 'Gender': [gender],
        'Green Fodder': [green_fodder], 'Type Green': [type_green], 'Qty Green': [qty_green],
        'Dry Fodder': [dry_fodder], 'Type Dry': [type_dry], 'Qty Dry': [qty_dry],
        'Concentrate Feed': [concentrate], 'Brand Concentrate': [brand_concentrate], 'Qty Concentrate': [qty_concentrate],
        'Mineral Mixture': [mineral], 'Brand Mineral': [brand_mineral], 'Qty Mineral': [qty_mineral],
        'Silage': [silage], 'Source and Price Silage': [source_price], 'Qty Silage': [qty_silage],
        'Water Source': [water_source]
    }

    df = pd.DataFrame(data)
    if os.path.exists(filepath):
        df.to_csv(filepath, mode='a', header=False, index=False)
    else:
        df.to_csv(filepath, index=False)

    st.success("✅ Response Saved!")

if os.path.exists('survey_responses/responses.csv'):
    st.header("📄 Past Submissions")
    all_data = pd.read_csv('survey_responses/responses.csv')
    st.dataframe(all_data)
    st.download_button("📥 Download Responses CSV", data=all_data.to_csv(index=False).encode('utf-8'), file_name='responses.csv')
