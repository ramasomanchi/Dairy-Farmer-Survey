# app.py (Streamlit Dairy Farmer Survey)

import streamlit as st
import pandas as pd
import datetime
import os

# --- Setup ---
st.set_page_config(page_title="Dairy Farmer Survey", page_icon="🐄", layout="centered")

# --- Translations ---
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
        'Submit': 'Submit',
    },
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
        'No. of Cattle in Milk': 'दूध में मवेशियों की संख्या',
        'No. of Calves/Heifers': 'बछड़ों/हेफर्स की संख्या',
        'No. of Desi Cows': 'देसी गायों की संख्या',
        'No. of Crossbreed Cows': 'क्रॉसब्रीड गायों की संख्या',
        'No. of Buffalo': 'भैंसों की संख्या',
        'Milk Production (liters/day)': 'दूध उत्पादन (लीटर/दिन)',
        'Type of Green Fodder': 'हरे चारे का प्रकार',
        'Quantity of Green Fodder (Kg/day)': 'हरे चारे की मात्रा (किलो/दिन)',
        'Type of Dry Fodder': 'सूखे चारे का प्रकार',
        'Quantity of Dry Fodder (Kg/day)': 'सूखे चारे की मात्रा (किलो/दिन)',
        'Brand of Concentrate Feed': 'सांद्रित फ़ीड का ब्रांड',
        'Quantity of Concentrate Feed (Kg/day)': 'सांद्रित फ़ीड की मात्रा (किलो/दिन)',
        'Brand of Mineral Mixture': 'खनिज मिश्रण का ब्रांड',
        'Quantity of Mineral Mixture (gm/day)': 'खनिज मिश्रण की मात्रा (ग्राम/दिन)',
        'Source and Price of Silage': 'साइलेज का स्रोत और मूल्य',
        'Quantity of Silage (Kg/day)': 'साइलेज की मात्रा (किलो/दिन)',
        'Source of Water': 'पानी का स्रोत',
        'Submit': 'जमा करें',
    },
    'Telugu': {
        'Farmer Name': 'రైతు పేరు',
        'Farmer Code': 'రైతు కోడ్',
        'Gender': 'లింగం',
        'Select Gender': 'లింగాన్ని ఎంచుకోండి',
        'Male': 'పురుషుడు',
        'Female': 'స్త్రీ',
        'HPC/MCC Name': 'హెచ్‌పిసి/ఎంసిసి పేరు',
        'HPC/MCC Code': 'హెచ్‌పిసి/ఎంసిసి కోడ్',
        'Type': 'రకం',
        'Select Type': 'రకం ఎంచుకోండి',
        'HPCC': 'హెచ్‌పిసిసి',
        'MCC': 'ఎంసిసి',
        'Number of Cows': 'ఆవుల సంఖ్య',
        'No. of Cattle in Milk': 'పాలలో పశువుల సంఖ్య',
        'No. of Calves/Heifers': 'దూడలు/హెఫర్స్ సంఖ్య',
        'No. of Desi Cows': 'దేశీ ఆవుల సంఖ్య',
        'No. of Crossbreed Cows': 'క్రాస్‌బ్రీడ్ ఆవుల సంఖ్య',
        'No. of Buffalo': 'గేదెల సంఖ్య',
        'Milk Production (liters/day)': 'పాల ఉత్పత్తి (లీటర్లు/రోజు)',
        'Type of Green Fodder': 'పచ్చి మేత రకం',
        'Quantity of Green Fodder (Kg/day)': 'పచ్చి మేత పరిమాణం (కిలోలు/రోజు)',
        'Type of Dry Fodder': 'పొడి మేత రకం',
        'Quantity of Dry Fodder (Kg/day)': 'పొడి మేత పరిమాణం (కిలోలు/రోజు)',
        'Brand of Concentrate Feed': 'సాంద్రీకృత ఫీడ్ బ్రాండ్',
        'Quantity of Concentrate Feed (Kg/day)': 'సాంద్రీకృత ఫీడ్ పరిమాణం (కిలోలు/రోజు)',
        'Brand of Mineral Mixture': 'ఖనిజ మిశ్రమం బ్రాండ్',
        'Quantity of Mineral Mixture (gm/day)': 'ఖనిజ మిశ్రమ పరిమాణం (గ్రాములు/రోజు)',
        'Source and Price of Silage': 'సైలేజ్ మూలం మరియు ధర',
        'Quantity of Silage (Kg/day)': 'సైలేజ్ పరిమాణం (కిలోలు/రోజు)',
        'Source of Water': 'నీటి మూలం',
        'Submit': 'సమర్పించండి',
    },
    'Marathi': {
        'Farmer Name': 'शेतकऱ्याचे नाव',
        'Farmer Code': 'शेतकरी कोड',
        'Gender': 'लिंग',
        'Select Gender': 'लिंग निवडा',
        'Male': 'पुरुष',
        'Female': 'स्त्री',
        'HPC/MCC Name': 'एचपीसी/एमसीसी नाव',
        'HPC/MCC Code': 'एचपीसी/एमसीसी कोड',
        'Type': 'प्रकार',
        'Select Type': 'प्रकार निवडा',
        'HPCC': 'एचपीसीसी',
        'MCC': 'एमसीसी',
        'Number of Cows': 'गायींची संख्या',
        'No. of Cattle in Milk': 'दुधात जनावरांची संख्या',
        'No. of Calves/Heifers': 'वासरांची संख्या',
        'No. of Desi Cows': 'देशी गायींची संख्या',
        'No. of Crossbreed Cows': 'संकरीत गायींची संख्या',
        'No. of Buffalo': 'म्हशींची संख्या',
        'Milk Production (liters/day)': 'दूध उत्पादन (लिटर/दिवस)',
        'Type of Green Fodder': 'हिरव्या चाऱ्याचा प्रकार',
        'Quantity of Green Fodder (Kg/day)': 'हिरव्या चाऱ्याचे प्रमाण (किलो/दिवस)',
        'Type of Dry Fodder': 'कोरड्या चाऱ्याचा प्रकार',
        'Quantity of Dry Fodder (Kg/day)': 'कोरड्या चाऱ्याचे प्रमाण (किलो/दिवस)',
        'Brand of Concentrate Feed': 'कॉन्सन्ट्रेट फीड ब्रँड',
        'Quantity of Concentrate Feed (Kg/day)': 'कॉन्सन्ट्रेट फीड प्रमाण (किलो/दिवस)',
        'Brand of Mineral Mixture': 'खनिज मिश्रण ब्रँड',
        'Quantity of Mineral Mixture (gm/day)': 'खनिज मिश्रण प्रमाण (ग्रॅम/दिवस)',
        'Source and Price of Silage': 'सायलेज स्रोत आणि किंमत',
        'Quantity of Silage (Kg/day)': 'सायलेज प्रमाण (किलो/दिवस)',
        'Source of Water': 'पाण्याचा स्रोत',
        'Submit': 'सबमिट करा',
    }
}

}

# --- Language Selection ---
lang = st.selectbox("Select Language / भाषा / భాష / भाषा", list(translations.keys()))
labels = translations[lang]

# --- Form Start ---
st.title("Dairy Farmer Survey")

with st.form("survey_form"):
    farmer_name = st.text_input(labels['Farmer Name'])
    farmer_code = st.text_input(labels['Farmer Code'])
    gender = st.selectbox(labels['Gender'], (labels['Male'], labels['Female']))
    hpc_mcc_name = st.text_input(labels['HPC/MCC Name'])
    hpc_mcc_code = st.text_input(labels['HPC/MCC Code'])
    farmer_type = st.selectbox(labels['Type'], (labels['HPCC'], labels['MCC']))
    
    number_of_cows = st.number_input(labels['Number of Cows'], min_value=0)
    cattle_in_milk = st.number_input(labels['No. of Cattle in Milk'], min_value=0)
    calves_heifers = st.number_input(labels['No. of Calves/Heifers'], min_value=0)
    desi_cows = st.number_input(labels['No. of Desi Cows'], min_value=0)
    crossbreed_cows = st.number_input(labels['No. of Crossbreed Cows'], min_value=0)
    buffaloes = st.number_input(labels['No. of Buffalo'], min_value=0)
    milk_production = st.number_input(labels['Milk Production (liters/day)'], min_value=0)

    green_fodder_type = st.text_input(labels['Type of Green Fodder'])
    green_fodder_qty = st.number_input(labels['Quantity of Green Fodder (Kg/day)'], min_value=0)
    dry_fodder_type = st.text_input(labels['Type of Dry Fodder'])
    dry_fodder_qty = st.number_input(labels['Quantity of Dry Fodder (Kg/day)'], min_value=0)
    concentrate_brand = st.text_input(labels['Brand of Concentrate Feed'])
    concentrate_qty = st.number_input(labels['Quantity of Concentrate Feed (Kg/day)'], min_value=0)
    mineral_brand = st.text_input(labels['Brand of Mineral Mixture'])
    mineral_qty = st.number_input(labels['Quantity of Mineral Mixture (gm/day)'], min_value=0)
    silage_source = st.text_input(labels['Source and Price of Silage'])
    silage_qty = st.number_input(labels['Quantity of Silage (Kg/day)'], min_value=0)
    water_source = st.text_input(labels['Source of Water'])

    submitted = st.form_submit_button(labels['Submit'])

# --- Saving Responses ---
if submitted:
    now = datetime.datetime.now()
    new_data = {
        'Timestamp': now.isoformat(),
        'Language': lang,
        'Farmer Name': farmer_name,
        'Farmer Code': farmer_code,
        'Gender': gender,
        'HPC/MCC Name': hpc_mcc_name,
        'HPC/MCC Code': hpc_mcc_code,
        'Type': farmer_type,
        'Number of Cows': number_of_cows,
        'No. of Cattle in Milk': cattle_in_milk,
        'No. of Calves/Heifers': calves_heifers,
        'No. of Desi Cows': desi_cows,
        'No. of Crossbreed Cows': crossbreed_cows,
        'No. of Buffalo': buffaloes,
        'Milk Production (liters/day)': milk_production,
        'Type of Green Fodder': green_fodder_type,
        'Quantity of Green Fodder (Kg/day)': green_fodder_qty,
        'Type of Dry Fodder': dry_fodder_type,
        'Quantity of Dry Fodder (Kg/day)': dry_fodder_qty,
        'Brand of Concentrate Feed': concentrate_brand,
        'Quantity of Concentrate Feed (Kg/day)': concentrate_qty,
        'Brand of Mineral Mixture': mineral_brand,
        'Quantity of Mineral Mixture (gm/day)': mineral_qty,
        'Source and Price of Silage': silage_source,
        'Quantity of Silage (Kg/day)': silage_qty,
        'Source of Water': water_source
    }
    save_dir = 'survey_submissions'
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, 'survey_data.csv')

    if os.path.exists(file_path):
        df_existing = pd.read_csv(file_path)
        df = pd.concat([df_existing, pd.DataFrame([new_data])], ignore_index=True)
    else:
        df = pd.DataFrame([new_data])

    df.to_csv(file_path, index=False)
    st.success("✅ Your response has been recorded!")

# --- View Past Submissions ---
if os.path.exists('survey_submissions/survey_data.csv'):
    st.header("View Past Submissions")
    data = pd.read_csv('survey_submissions/survey_data.csv')
    st.dataframe(data)
    st.download_button("Download Data as CSV", data.to_csv(index=False), file_name="survey_data.csv")
else:
    st.info("No submissions found yet.")

# --- End of app.py ---
