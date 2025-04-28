# app.py

import streamlit as st
import pandas as pd
import datetime
import os

# --- Full Translations ---
translations = {
    'English': {
        'Farmer Name': 'Farmer Name', 'Farmer Code': 'Farmer Code', 'Gender': 'Gender',
        'Select Gender': 'Select Gender', 'Male': 'Male', 'Female': 'Female',
        'Type': 'Type', 'Select Type': 'Select Type', 'HPCC': 'HPCC', 'MCC': 'MCC',
        'Number of Cows': 'Number of Cows', 'No. of Cattle in Milk': 'No. of Cattle in Milk',
        'No. of Calves/Heifers': 'No. of Calves/Heifers', 'No. of Desi Cows': 'No. of Desi Cows',
        'No. of Crossbreed Cows': 'No. of Crossbreed Cows', 'No. of Buffalo': 'No. of Buffalo',
        'Milk Production': 'Milk Production (liters/day)',
        'Type of Green Fodder': 'Type of Green Fodder', 'Green Fodder Quantity': 'Quantity of Green Fodder (Kg/day)',
        'Type of Dry Fodder': 'Type of Dry Fodder', 'Dry Fodder Quantity': 'Quantity of Dry Fodder (Kg/day)',
        'Brand of Concentrate Feed': 'Brand of Concentrate Feed', 'Concentrate Quantity': 'Quantity of Concentrate Feed (Kg/day)',
        'Brand of Mineral Mixture': 'Brand of Mineral Mixture', 'Mineral Mixture Quantity': 'Quantity of Mineral Mixture (gm/day)',
        'Source and Price of Silage': 'Source and Price of Silage', 'Quantity of Silage': 'Quantity of Silage (Kg/day)',
        'Source of Water': 'Source of Water', 'Submit': 'Submit', 'Language': 'Language',
        'Green Fodder': 'Green Fodder Available?', 'Dry Fodder': 'Dry Fodder Available?',
        'Concentrate Feed': 'Concentrate Feed Available?', 'Mineral Mixture': 'Mineral Mixture Available?',
        'Silage': 'Silage Available?', 'Yes': 'Yes', 'No': 'No'
    },
    'Hindi': {
        'Farmer Name': 'किसान का नाम', 'Farmer Code': 'किसान कोड', 'Gender': 'लिंग',
        'Select Gender': 'लिंग चुनें', 'Male': 'पुरुष', 'Female': 'महिला',
        'Type': 'प्रकार', 'Select Type': 'प्रकार चुनें', 'HPCC': 'एचपीसीसी', 'MCC': 'एमसीसी',
        'Number of Cows': 'गायों की संख्या', 'No. of Cattle in Milk': 'दूध में मवेशियों की संख्या',
        'No. of Calves/Heifers': 'बछड़ों/हेफर्स की संख्या', 'No. of Desi Cows': 'देसी गायों की संख्या',
        'No. of Crossbreed Cows': 'क्रॉसब्रीड गायों की संख्या', 'No. of Buffalo': 'भैंसों की संख्या',
        'Milk Production': 'दूध उत्पादन (लीटर/दिन)',
        'Type of Green Fodder': 'हरे चारे का प्रकार', 'Green Fodder Quantity': 'हरे चारे की मात्रा (किलो/दिन)',
        'Type of Dry Fodder': 'सूखे चारे का प्रकार', 'Dry Fodder Quantity': 'सूखे चारे की मात्रा (किलो/दिन)',
        'Brand of Concentrate Feed': 'सांद्रित फ़ीड का ब्रांड', 'Concentrate Quantity': 'सांद्रित फ़ीड की मात्रा (किलो/दिन)',
        'Brand of Mineral Mixture': 'खनिज मिश्रण का ब्रांड', 'Mineral Mixture Quantity': 'खनिज मिश्रण की मात्रा (ग्राम/दिन)',
        'Source and Price of Silage': 'साइलेज का स्रोत और मूल्य', 'Quantity of Silage': 'साइलेज की मात्रा (किलो/दिन)',
        'Source of Water': 'पानी का स्रोत', 'Submit': 'जमा करें', 'Language': 'भाषा',
        'Green Fodder': 'हरा चारा उपलब्ध है?', 'Dry Fodder': 'सूखा चारा उपलब्ध है?',
        'Concentrate Feed': 'सांद्रित फ़ीड उपलब्ध है?', 'Mineral Mixture': 'खनिज मिश्रण उपलब्ध है?',
        'Silage': 'साइलेज उपलब्ध है?', 'Yes': 'हाँ', 'No': 'नहीं'
    },
    'Telugu': {
        'Farmer Name': 'రైతు పేరు', 'Farmer Code': 'రైతు కోడ్', 'Gender': 'లింగం',
        'Select Gender': 'లింగాన్ని ఎంచుకోండి', 'Male': 'పురుషుడు', 'Female': 'స్త్రీ',
        'Type': 'రకం', 'Select Type': 'రకం ఎంచుకోండి', 'HPCC': 'హెచ్‌పిసిసి', 'MCC': 'ఎంసిసి',
        'Number of Cows': 'ఆవుల సంఖ్య', 'No. of Cattle in Milk': 'పాలలో పశువుల సంఖ్య',
        'No. of Calves/Heifers': 'దూడలు/హెఫర్లు సంఖ్య', 'No. of Desi Cows': 'దేశీ ఆవుల సంఖ్య',
        'No. of Crossbreed Cows': 'క్రాస్‌బ్రీడ్ ఆవుల సంఖ్య', 'No. of Buffalo': 'గేదెల సంఖ్య',
        'Milk Production': 'పాల ఉత్పత్తి (లీటర్లు/రోజు)',
        'Type of Green Fodder': 'పచ్చి మేత రకం', 'Green Fodder Quantity': 'పచ్చి మేత పరిమాణం (కిలోలు/రోజు)',
        'Type of Dry Fodder': 'పొడి మేత రకం', 'Dry Fodder Quantity': 'పొడి మేత పరిమాణం (కిలోలు/రోజు)',
        'Brand of Concentrate Feed': 'సాంద్రీకృత దాణా బ్రాండ్', 'Concentrate Quantity': 'సాంద్రీకృత దాణా పరిమాణం (కిలోలు/రోజు)',
        'Brand of Mineral Mixture': 'ఖనిజ మిశ్రమం బ్రాండ్', 'Mineral Mixture Quantity': 'ఖనిజ మిశ్రమం పరిమాణం (గ్రాములు/రోజు)',
        'Source and Price of Silage': 'సైలేజ్ మూలం మరియు ధర', 'Quantity of Silage': 'సైలేజ్ పరిమాణం (కిలోలు/రోజు)',
        'Source of Water': 'నీటి మూలం', 'Submit': 'సమర్పించండి', 'Language': 'భాష',
        'Green Fodder': 'పచ్చి మేత అందుబాటులో ఉందా?', 'Dry Fodder': 'పొడి మేత అందుబాటులో ఉందా?',
        'Concentrate Feed': 'సాంద్రీకృత దాణా అందుబాటులో ఉందా?', 'Mineral Mixture': 'ఖనిజ మిశ్రమం అందుబాటులో ఉందా?',
        'Silage': 'సైలేజ్ అందుబాటులో ఉందా?', 'Yes': 'అవును', 'No': 'లేదు'
    },
    'Marathi': {
        'Farmer Name': 'शेतकऱ्याचे नाव', 'Farmer Code': 'शेतकरी कोड', 'Gender': 'लिंग',
        'Select Gender': 'लिंग निवडा', 'Male': 'पुरुष', 'Female': 'स्त्री',
        'Type': 'प्रकार', 'Select Type': 'प्रकार निवडा', 'HPCC': 'एचपीसीसी', 'MCC': 'एमसीसी',
        'Number of Cows': 'गायींची संख्या', 'No. of Cattle in Milk': 'दुधात जनावरांची संख्या',
        'No. of Calves/Heifers': 'वासरांची संख्या', 'No. of Desi Cows': 'देशी गायींची संख्या',
        'No. of Crossbreed Cows': 'संकरीत गायींची संख्या', 'No. of Buffalo': 'म्हशींची संख्या',
        'Milk Production': 'दूध उत्पादन (लिटर/दिवस)',
        'Type of Green Fodder': 'हिरव्या चाऱ्याचा प्रकार', 'Green Fodder Quantity': 'हिरव्या चाऱ्याचे प्रमाण (किलो/दिवस)',
        'Type of Dry Fodder': 'कोरड्या चाऱ्याचा प्रकार', 'Dry Fodder Quantity': 'कोरड्या चाऱ्याचे प्रमाण (किलो/दिवस)',
        'Brand of Concentrate Feed': 'कॉन्सन्ट्रेट फीड ब्रँड', 'Concentrate Quantity': 'कॉन्सन्ट्रेट फीड प्रमाण (किलो/दिवस)',
        'Brand of Mineral Mixture': 'खनिज मिश्रण ब्रँड', 'Mineral Mixture Quantity': 'खनिज मिश्रण प्रमाण (ग्रॅम/दिवस)',
        'Source and Price of Silage': 'सायलेज स्रोत आणि किंमत', 'Quantity of Silage': 'सायलेज प्रमाण (किलो/दिवस)',
        'Source of Water': 'पाण्याचा स्रोत', 'Submit': 'सबमिट करा', 'Language': 'भाषा',
        'Green Fodder': 'हिरवा चारा उपलब्ध आहे का?', 'Dry Fodder': 'कोरडा चारा उपलब्ध आहे का?',
        'Concentrate Feed': 'कॉन्सन्ट्रेट फीड उपलब्ध आहे का?', 'Mineral Mixture': 'खनिज मिश्रण उपलब्ध आहे का?',
        'Silage': 'सायलेज उपलब्ध आहे का?', 'Yes': 'होय', 'No': 'नाही'
    }
}

# --- App starts here ---
st.set_page_config(page_title="Dairy Farmer Survey", page_icon="🐄", layout="centered")

st.title("🐄 Dairy Farmer Survey")

# Language selection
lang = st.selectbox("Language", list(translations.keys()))
labels = translations.get(lang, translations['English'])

# Form
with st.form("survey_form"):
    farmer_name = st.text_input(labels['Farmer Name'])
    farmer_code = st.text_input(labels['Farmer Code'])
    gender = st.selectbox(labels['Gender'], [labels['Male'], labels['Female']])
    type_ = st.selectbox(labels['Type'], [labels['HPCC'], labels['MCC']])
    number_of_cows = st.number_input(labels['Number of Cows'], min_value=0)
    cattle_in_milk = st.number_input(labels['No. of Cattle in Milk'], min_value=0)
    calves_heifers = st.number_input(labels['No. of Calves/Heifers'], min_value=0)
    desi_cows = st.number_input(labels['No. of Desi Cows'], min_value=0)
    crossbreed_cows = st.number_input(labels['No. of Crossbreed Cows'], min_value=0)
    buffaloes = st.number_input(labels['No. of Buffalo'], min_value=0)
    milk_production = st.number_input(labels['Milk Production'], min_value=0)
    
    type_green_fodder = st.text_input(labels['Type of Green Fodder'])
    green_fodder_qty = st.number_input(labels['Green Fodder Quantity'], min_value=0)
    type_dry_fodder = st.text_input(labels['Type of Dry Fodder'])
    dry_fodder_qty = st.number_input(labels['Dry Fodder Quantity'], min_value=0)
    brand_concentrate = st.text_input(labels['Brand of Concentrate Feed'])
    concentrate_qty = st.number_input(labels['Concentrate Quantity'], min_value=0)
    brand_mineral = st.text_input(labels['Brand of Mineral Mixture'])
    mineral_qty = st.number_input(labels['Mineral Mixture Quantity'], min_value=0)
    silage_source = st.text_input(labels['Source and Price of Silage'])
    silage_qty = st.number_input(labels['Quantity of Silage'], min_value=0)
    water_source = st.text_input(labels['Source of Water'])

    submitted = st.form_submit_button(labels['Submit'])

# --- Handle Form Submission ---
if submitted:
    folder = 'survey_submissions'
    os.makedirs(folder, exist_ok=True)

    data = {
        'Timestamp': datetime.datetime.now().isoformat(),
        'Language': lang,
        'Farmer Name': farmer_name,
        'Farmer Code': farmer_code,
        'Gender': gender,
        'Type': type_,
        'Number of Cows': number_of_cows,
        'No. of Cattle in Milk': cattle_in_milk,
        'No. of Calves/Heifers': calves_heifers,
        'No. of Desi Cows': desi_cows,
        'No. of Crossbreed Cows': crossbreed_cows,
        'No. of Buffalo': buffaloes,
        'Milk Production (liters/day)': milk_production,
        'Type of Green Fodder': type_green_fodder,
        'Quantity of Green Fodder (Kg/day)': green_fodder_qty,
        'Type of Dry Fodder': type_dry_fodder,
        'Quantity of Dry Fodder (Kg/day)': dry_fodder_qty,
        'Brand of Concentrate Feed': brand_concentrate,
        'Quantity of Concentrate Feed (Kg/day)': concentrate_qty,
        'Brand of Mineral Mixture': brand_mineral,
        'Quantity of Mineral Mixture (gm/day)': mineral_qty,
        'Source and Price of Silage': silage_source,
        'Quantity of Silage (Kg/day)': silage_qty,
        'Source of Water': water_source
    }

    df = pd.DataFrame([data])

    if os.path.exists(f"{folder}/survey_data.csv"):
        df.to_csv(f"{folder}/survey_data.csv", mode='a', header=False, index=False)
    else:
        df.to_csv(f"{folder}/survey_data.csv", index=False)

    st.success("✅ Submission saved!")
    st.download_button("📥 Download your submission", df.to_csv(index=False).encode('utf-8'), "submission.csv")

# --- View Previous Submissions ---
st.header("📄 Past Submissions")
if os.path.exists(f"{folder}/survey_data.csv"):
    df = pd.read_csv(f"{folder}/survey_data.csv")
    st.dataframe(df)
else:
    st.info("No submissions yet!")
