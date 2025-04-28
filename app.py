# app.py (Final Streamlit Dairy Survey)

import streamlit as st
import pandas as pd
import datetime
import os

# Translations
translations = {
    'English': {
        'Language': 'Language',
        'Farmer Profile': 'Farmer Profile',
        'HPC/MCC Name': 'HPC/MCC Name',
        'HPC/MCC Code': 'HPC/MCC Code',
        'Types': 'Types',
        'HPCC': 'HPCC',
        'MCC': 'MCC',
        'Farmer Name': 'Farmer Name',
        'Farmer Code': 'Farmer Code / Pourer Id',
        'Gender': 'Gender',
        'Male': 'Male',
        'Female': 'Female',
        'Farm Details': 'Farm Details',
        'Number of Cows': 'Number of Cows',
        'No. of Cattle in Milk': 'No. of Cattle in Milk',
        'No. of Calves/Heifers': 'No. of Calves/Heifers',
        'No. of Desi cows': 'No. of Desi cows',
        'No. of Cross breed cows': 'No. of Cross breed cows',
        'No. of Buffalo': 'No. of Buffalo',
        'Milk Production': 'Milk Production in liters/day',
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
        'Name of Surveyor': 'Name of Surveyor',
        'Date of Visit': 'Date of Visit',
        'Submit': 'Submit',
        'Yes': 'Yes',
        'No': 'No',
        'Download CSV': 'Download CSV'
    },
    'Hindi': {
        'Language': 'भाषा',
        'Farmer Profile': 'किसान प्रोफ़ाइल',
        'HPC/MCC Name': 'एचपीसी/एमसीसी नाम',
        'HPC/MCC Code': 'एचपीसी/एमसीसी कोड',
        'Types': 'प्रकार',
        'HPCC': 'एचपीसीसी',
        'MCC': 'एमसीसी',
        'Farmer Name': 'किसान का नाम',
        'Farmer Code': 'किसान कोड / पौरर आईडी',
        'Gender': 'लिंग',
        'Male': 'पुरुष',
        'Female': 'महिला',
        'Farm Details': 'फार्म विवरण',
        'Number of Cows': 'गायों की संख्या',
        'No. of Cattle in Milk': 'दूध देने वाली गायें',
        'No. of Calves/Heifers': 'बछड़े/हीफर की संख्या',
        'No. of Desi cows': 'देसी गायों की संख्या',
        'No. of Cross breed cows': 'क्रॉसब्रीड गायों की संख्या',
        'No. of Buffalo': 'भैंसों की संख्या',
        'Milk Production': 'दूध उत्पादन (लीटर/दिन)',
        'Specific Questions': 'विशिष्ट प्रश्न',
        'Green Fodder': 'हरा चारा',
        'Type of Green Fodder': 'हरे चारे का प्रकार',
        'Quantity of Green Fodder': 'हरे चारे की मात्रा (किलो/दिन)',
        'Dry Fodder': 'सूखा चारा',
        'Type of Dry Fodder': 'सूखे चारे का प्रकार',
        'Quantity of Dry Fodder': 'सूखे चारे की मात्रा (किलो/दिन)',
        'Concentrate Feed': 'सांद्रित चारा',
        'Brand of Concentrate Feed': 'सांद्रित चारे का ब्रांड',
        'Quantity of Concentrate Feed': 'सांद्रित चारे की मात्रा (किलो/दिन)',
        'Mineral Mixture': 'खनिज मिश्रण',
        'Brand of Mineral Mixture': 'खनिज मिश्रण का ब्रांड',
        'Quantity of Mineral Mixture': 'खनिज मिश्रण की मात्रा (ग्राम/दिन)',
        'Silage': 'साइलेज',
        'Source and Price of Silage': 'साइलेज का स्रोत और कीमत',
        'Quantity of Silage': 'साइलेज की मात्रा (किलो/दिन)',
        'Source of Water': 'पानी का स्रोत',
        'Name of Surveyor': 'सर्वेक्षक का नाम',
        'Date of Visit': 'दौरे की तारीख',
        'Submit': 'जमा करें',
        'Yes': 'हाँ',
        'No': 'नहीं',
        'Download CSV': 'CSV डाउनलोड करें'
    }
}

# Set up survey storage
SAVE_DIR = "survey_responses"
os.makedirs(SAVE_DIR, exist_ok=True)
SAVE_PATH = os.path.join(SAVE_DIR, "responses.csv")

# Streamlit UI
st.set_page_config(page_title="Dairy Survey", page_icon="🐄", layout="centered")

lang = st.selectbox("Select Language", ("English", "Hindi"))
labels = translations[lang]

st.title(labels['Farmer Profile'])
hpc_name = st.text_input(labels['HPC/MCC Name'])
hpc_code = st.text_input(labels['HPC/MCC Code'])
type_hpc = st.selectbox(labels['Types'], (labels['HPCC'], labels['MCC']))
farmer_name = st.text_input(labels['Farmer Name'])
farmer_code = st.text_input(labels['Farmer Code'])
gender = st.selectbox(labels['Gender'], (labels['Male'], labels['Female']))

st.markdown("---")
st.header(labels['Farm Details'])
num_cows = st.number_input(labels['Number of Cows'], 0)
num_cattle_milk = st.number_input(labels['No. of Cattle in Milk'], 0)
num_calves = st.number_input(labels['No. of Calves/Heifers'], 0)
num_desi_cows = st.number_input(labels['No. of Desi cows'], 0)
num_cross_cows = st.number_input(labels['No. of Cross breed cows'], 0)
num_buffalo = st.number_input(labels['No. of Buffalo'], 0)
milk_production = st.number_input(labels['Milk Production'], 0)

st.markdown("---")
st.header(labels['Specific Questions'])

# Specific Qs
green_fodder = st.selectbox(labels['Green Fodder'], (labels['Yes'], labels['No']))
green_fodder_type = st.text_input(labels['Type of Green Fodder']) if green_fodder == labels['Yes'] else ""
green_fodder_qty = st.number_input(labels['Quantity of Green Fodder'], 0)

dry_fodder = st.selectbox(labels['Dry Fodder'], (labels['Yes'], labels['No']))
dry_fodder_type = st.text_input(labels['Type of Dry Fodder']) if dry_fodder == labels['Yes'] else ""
dry_fodder_qty = st.number_input(labels['Quantity of Dry Fodder'], 0)

concentrate_feed = st.selectbox(labels['Concentrate Feed'], (labels['Yes'], labels['No']))
conc_feed_brand = st.text_input(labels['Brand of Concentrate Feed']) if concentrate_feed == labels['Yes'] else ""
conc_feed_qty = st.number_input(labels['Quantity of Concentrate Feed'], 0)

mineral_mixture = st.selectbox(labels['Mineral Mixture'], (labels['Yes'], labels['No']))
mineral_brand = st.text_input(labels['Brand of Mineral Mixture']) if mineral_mixture == labels['Yes'] else ""
mineral_qty = st.number_input(labels['Quantity of Mineral Mixture'], 0)

silage = st.selectbox(labels['Silage'], (labels['Yes'], labels['No']))
silage_src_price = st.text_input(labels['Source and Price of Silage']) if silage == labels['Yes'] else ""
silage_qty = st.number_input(labels['Quantity of Silage'], 0)

water_source = st.text_input(labels['Source of Water'])

st.markdown("---")
surveyor = st.text_input(labels['Name of Surveyor'])
visit_date = st.date_input(labels['Date of Visit'])

if st.button(labels['Submit']):
    new_entry = {
        'Timestamp': datetime.datetime.now(),
        'Language': lang,
        'HPC/MCC Name': hpc_name,
        'HPC/MCC Code': hpc_code,
        'Type': type_hpc,
        'Farmer Name': farmer_name,
        'Farmer Code': farmer_code,
        'Gender': gender,
        'Number of Cows': num_cows,
        'No. of Cattle in Milk': num_cattle_milk,
        'No. of Calves/Heifers': num_calves,
        'No. of Desi cows': num_desi_cows,
        'No. of Cross breed cows': num_cross_cows,
        'No. of Buffalo': num_buffalo,
        'Milk Production': milk_production,
        'Green Fodder': green_fodder,
        'Type of Green Fodder': green_fodder_type,
        'Quantity of Green Fodder': green_fodder_qty,
        'Dry Fodder': dry_fodder,
        'Type of Dry Fodder': dry_fodder_type,
        'Quantity of Dry Fodder': dry_fodder_qty,
        'Concentrate Feed': concentrate_feed,
        'Brand of Concentrate Feed': conc_feed_brand,
        'Quantity of Concentrate Feed': conc_feed_qty,
        'Mineral Mixture': mineral_mixture,
        'Brand of Mineral Mixture': mineral_brand,
        'Quantity of Mineral Mixture': mineral_qty,
        'Silage': silage,
        'Source and Price of Silage': silage_src_price,
        'Quantity of Silage': silage_qty,
        'Source of Water': water_source,
        'Name of Surveyor': surveyor,
        'Date of Visit': visit_date
    }
    df = pd.DataFrame([new_entry])
    if os.path.exists(SAVE_PATH):
        df.to_csv(SAVE_PATH, mode='a', header=False, index=False)
    else:
        df.to_csv(SAVE_PATH, index=False)
    st.success("✅ Submitted successfully!")

# View past submissions
if os.path.exists(SAVE_PATH):
    st.markdown("---")
    st.header("View Submissions")
    past_df = pd.read_csv(SAVE_PATH)
    st.dataframe(past_df)

    # Download button
    st.download_button(
        label=labels['Download CSV'],
        data=past_df.to_csv(index=False),
        file_name='survey_responses.csv',
        mime='text/csv'
    )
