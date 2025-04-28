# app.py

import streamlit as st
import pandas as pd
import datetime
import os

# Full Multilingual Translations
dict_translations = {
    'English': {
        'Farmer Name': 'Farmer Name', 'Farmer Code': 'Farmer Code', 'Gender': 'Gender',
        'HPC/MCC Name': 'HPC/MCC Name', 'HPC/MCC Code': 'HPC/MCC Code', 'Type': 'Type',
        'Number of Cows': 'Number of Cows', 'No. of Cattle in Milk': 'No. of Cattle in Milk',
        'No. of Calves/Heifers': 'No. of Calves/Heifers', 'No. of Desi Cows': 'No. of Desi Cows',
        'No. of Crossbreed Cows': 'No. of Crossbreed Cows', 'No. of Buffalo': 'No. of Buffalo',
        'Milk Production (liters/day)': 'Milk Production (liters/day)',
        'Type of Green Fodder': 'Type of Green Fodder',
        'Quantity of Green Fodder (Kg/day)': 'Quantity of Green Fodder (Kg/day)',
        'Type of Dry Fodder': 'Type of Dry Fodder',
        'Quantity of Dry Fodder (Kg/day)': 'Quantity of Dry Fodder (Kg/day)',
        'Brand of Concentrate Feed': 'Brand of Concentrate Feed',
        'Quantity of Concentrate Feed (Kg/day)': 'Quantity of Concentrate Feed (Kg/day)',
        'Brand of Mineral Mixture': 'Brand of Mineral Mixture',
        'Quantity of Mineral Mixture (gm/day)': 'Quantity of Mineral Mixture (gm/day)',
        'Source and Price of Silage': 'Source and Price of Silage',
        'Quantity of Silage (Kg/day)': 'Quantity of Silage (Kg/day)',
        'Source of Water': 'Source of Water',
        'Green Fodder Available?': 'Green Fodder Available?', 'Dry Fodder Available?': 'Dry Fodder Available?',
        'Concentrate Feed Available?': 'Concentrate Feed Available?', 'Mineral Mixture Available?': 'Mineral Mixture Available?',
        'Silage Available?': 'Silage Available?', 'Language': 'Language',
        'Select Gender': 'Select Gender', 'Select Type': 'Select Type',
        'Male': 'Male', 'Female': 'Female', 'HPCC': 'HPCC', 'MCC': 'MCC',
        'Yes': 'Yes', 'No': 'No', 'Submit': 'Submit'
    },
    'Hindi': {
        'Farmer Name': 'किसान का नाम', 'Farmer Code': 'किसान कोड', 'Gender': 'लिंग',
        'HPC/MCC Name': 'एचपीसी/एमसीसी नाम', 'HPC/MCC Code': 'एचपीसी/एमसीसी कोड', 'Type': 'प्रकार',
        'Number of Cows': 'गायों की संख्या', 'No. of Cattle in Milk': 'दूध में मवेशियों की संख्या',
        'No. of Calves/Heifers': 'बछड़ों/हेफर्स की संख्या', 'No. of Desi Cows': 'देसी गायों की संख्या',
        'No. of Crossbreed Cows': 'क्रॉसब्रीड गायों की संख्या', 'No. of Buffalo': 'भैंसों की संख्या',
        'Milk Production (liters/day)': 'दूध उत्पादन (लीटर/दिन)', 'Type of Green Fodder': 'हरे चारे का प्रकार',
        'Quantity of Green Fodder (Kg/day)': 'हरे चारे की मात्रा (किलो/दिन)',
        'Type of Dry Fodder': 'सूखे चारे का प्रकार', 'Quantity of Dry Fodder (Kg/day)': 'सूखे चारे की मात्रा (किलो/दिन)',
        'Brand of Concentrate Feed': 'सांद्रित फ़ीड का ब्रांड',
        'Quantity of Concentrate Feed (Kg/day)': 'सांद्रित फ़ीड की मात्रा (किलो/दिन)',
        'Brand of Mineral Mixture': 'खनिज मिश्रण का ब्रांड',
        'Quantity of Mineral Mixture (gm/day)': 'खनिज मिश्रण की मात्रा (ग्राम/दिन)',
        'Source and Price of Silage': 'साइलेज का स्रोत और मूल्य',
        'Quantity of Silage (Kg/day)': 'साइलेज की मात्रा (किलो/दिन)',
        'Source of Water': 'पानी का स्रोत', 'Green Fodder Available?': 'हरा चारा उपलब्ध है?',
        'Dry Fodder Available?': 'सूखा चारा उपलब्ध है?', 'Concentrate Feed Available?': 'सांद्रित फ़ीड उपलब्ध है?',
        'Mineral Mixture Available?': 'खनिज मिश्रण उपलब्ध है?', 'Silage Available?': 'साइलेज उपलब्ध है?',
        'Language': 'भाषा', 'Select Gender': 'लिंग चुनें', 'Select Type': 'प्रकार चुनें',
        'Male': 'पुरुष', 'Female': 'महिला', 'HPCC': 'एचपीसीसी', 'MCC': 'एमसीसी',
        'Yes': 'हाँ', 'No': 'नहीं', 'Submit': 'जमा करें'
    },
    # (similarly add Telugu and Marathi like above)
}

st.set_page_config(page_title="Dairy Survey", page_icon="🐄", layout="centered")

lang = st.selectbox("Language / भाषा / భాష / भाषा", list(dict_translations.keys()))
labels = dict_translations.get(lang, dict_translations['English'])

st.title(f"{labels['Farmer Name']} ✨ {labels['Farmer Code']}")

with st.form("survey_form"):
    farmer_name = st.text_input(labels['Farmer Name'])
    farmer_code = st.text_input(labels['Farmer Code'])
    gender = st.selectbox(labels['Gender'], (labels['Male'], labels['Female']))
    hpc_name = st.text_input(labels['HPC/MCC Name'])
    hpc_code = st.text_input(labels['HPC/MCC Code'])
    type_ = st.selectbox(labels['Type'], (labels['HPCC'], labels['MCC']))
    no_cows = st.number_input(labels['Number of Cows'], 0)
    cattle_in_milk = st.number_input(labels['No. of Cattle in Milk'], 0)
    calves = st.number_input(labels['No. of Calves/Heifers'], 0)
    desi_cows = st.number_input(labels['No. of Desi Cows'], 0)
    crossbreed_cows = st.number_input(labels['No. of Crossbreed Cows'], 0)
    buffalo = st.number_input(labels['No. of Buffalo'], 0)
    milk_production = st.number_input(labels['Milk Production (liters/day)'], 0)
    green_fodder_avail = st.selectbox(labels['Green Fodder Available?'], (labels['Yes'], labels['No']))
    type_green_fodder = st.text_input(labels['Type of Green Fodder'])
    qty_green_fodder = st.number_input(labels['Quantity of Green Fodder (Kg/day)'], 0)
    dry_fodder_avail = st.selectbox(labels['Dry Fodder Available?'], (labels['Yes'], labels['No']))
    type_dry_fodder = st.text_input(labels['Type of Dry Fodder'])
    qty_dry_fodder = st.number_input(labels['Quantity of Dry Fodder (Kg/day)'], 0)
    concentrate_avail = st.selectbox(labels['Concentrate Feed Available?'], (labels['Yes'], labels['No']))
    brand_concentrate = st.text_input(labels['Brand of Concentrate Feed'])
    qty_concentrate = st.number_input(labels['Quantity of Concentrate Feed (Kg/day)'], 0)
    mineral_avail = st.selectbox(labels['Mineral Mixture Available?'], (labels['Yes'], labels['No']))
    brand_mineral = st.text_input(labels['Brand of Mineral Mixture'])
    qty_mineral = st.number_input(labels['Quantity of Mineral Mixture (gm/day)'], 0)
    silage_avail = st.selectbox(labels['Silage Available?'], (labels['Yes'], labels['No']))
    source_silage = st.text_input(labels['Source and Price of Silage'])
    qty_silage = st.number_input(labels['Quantity of Silage (Kg/day)'], 0)
    source_water = st.text_input(labels['Source of Water'])

    submit = st.form_submit_button(labels['Submit'])

if submit:
    now = datetime.datetime.now()
    data = {
        'Timestamp': [now.isoformat()],
        'Language': [lang],
        'Farmer Name': [farmer_name],
        'Farmer Code': [farmer_code],
        'Gender': [gender],
        'HPC/MCC Name': [hpc_name],
        'HPC/MCC Code': [hpc_code],
        'Type': [type_],
        'Number of Cows': [no_cows],
        'No. of Cattle in Milk': [cattle_in_milk],
        'No. of Calves/Heifers': [calves],
        'No. of Desi Cows': [desi_cows],
        'No. of Crossbreed Cows': [crossbreed_cows],
        'No. of Buffalo': [buffalo],
        'Milk Production (liters/day)': [milk_production],
        'Green Fodder Available?': [green_fodder_avail],
        'Type of Green Fodder': [type_green_fodder],
        'Quantity of Green Fodder (Kg/day)': [qty_green_fodder],
        'Dry Fodder Available?': [dry_fodder_avail],
        'Type of Dry Fodder': [type_dry_fodder],
        'Quantity of Dry Fodder (Kg/day)': [qty_dry_fodder],
        'Concentrate Feed Available?': [concentrate_avail],
        'Brand of Concentrate Feed': [brand_concentrate],
        'Quantity of Concentrate Feed (Kg/day)': [qty_concentrate],
        'Mineral Mixture Available?': [mineral_avail],
        'Brand of Mineral Mixture': [brand_mineral],
        'Quantity of Mineral Mixture (gm/day)': [qty_mineral],
        'Silage Available?': [silage_avail],
        'Source and Price of Silage': [source_silage],
        'Quantity of Silage (Kg/day)': [qty_silage],
        'Source of Water': [source_water]
    }
    df = pd.DataFrame(data)
    if os.path.exists("survey_data.csv"):
        df.to_csv("survey_data.csv", mode='a', header=False, index=False, encoding='utf-8')
    else:
        df.to_csv("survey_data.csv", index=False, encoding='utf-8')

    st.success("✅ Survey Saved Successfully!")
