# app.py (Dairy Survey Full Expanded - Multilingual)

import streamlit as st
import pandas as pd
import datetime
import os

# Translation Dictionary
translations = {
    'English': {
        'Farmer Profile': 'Farmer Profile',
        'Farm Details': 'Farm Details',
        'Specific Questions': 'Specific Questions',
        'HPC/MCC Name': 'HPC/MCC Name',
        'HPC/MCC Code': 'HPC/MCC Code',
        'Type': 'Type',
        'HPCC': 'HPCC',
        'MCC': 'MCC',
        'Farmer Name': 'Farmer Name',
        'Farmer Code': 'Farmer Code / Pourer ID',
        'Gender': 'Gender',
        'Male': 'Male',
        'Female': 'Female',
        'Number of Cows': 'Number of Cows',
        'No. of Cattle in Milk': 'No. of Cattle in Milk',
        'No. of Calves/Heifers': 'No. of Calves/Heifers',
        'No. of Desi Cows': 'No. of Desi Cows',
        'No. of Crossbreed Cows': 'No. of Crossbreed Cows',
        'No. of Buffalo': 'No. of Buffalo',
        'Milk Production': 'Milk Production (liters/day)',
        'Green Fodder': 'Green Fodder Available?',
        'Type of Green Fodder': 'Type of Green Fodder',
        'Quantity of Green Fodder': 'Quantity of Green Fodder (Kg/day)',
        'Dry Fodder': 'Dry Fodder Available?',
        'Type of Dry Fodder': 'Type of Dry Fodder',
        'Quantity of Dry Fodder': 'Quantity of Dry Fodder (Kg/day)',
        'Concentrate Feed': 'Concentrate Feed Available?',
        'Brand of Concentrate Feed': 'Brand of Concentrate Feed',
        'Quantity of Concentrate Feed': 'Quantity of Concentrate Feed (Kg/day)',
        'Mineral Mixture': 'Mineral Mixture Available?',
        'Brand of Mineral Mixture': 'Brand of Mineral Mixture',
        'Quantity of Mineral Mixture': 'Quantity of Mineral Mixture (gm/day)',
        'Silage': 'Silage Available?',
        'Source and Price of Silage': 'Source and Price of Silage',
        'Quantity of Silage': 'Quantity of Silage (Kg/day)',
        'Source of Water': 'Source of Water',
        'Submit': 'Submit',
        'Download CSV': 'Download CSV',
        'Select Language': 'Select Language',
    },
    'Hindi': {
        'Farmer Profile': 'किसान प्रोफ़ाइल',
        'Farm Details': 'फ़ार्म विवरण',
        'Specific Questions': 'विशेष प्रश्न',
        'HPC/MCC Name': 'एचपीसी/एमसीसी नाम',
        'HPC/MCC Code': 'एचपीसी/एमसीसी कोड',
        'Type': 'प्रकार',
        'HPCC': 'एचपीसीसी',
        'MCC': 'एमसीसी',
        'Farmer Name': 'किसान का नाम',
        'Farmer Code': 'किसान कोड / पौरर आईडी',
        'Gender': 'लिंग',
        'Male': 'पुरुष',
        'Female': 'महिला',
        'Number of Cows': 'गायों की संख्या',
        'No. of Cattle in Milk': 'दूध में मवेशी',
        'No. of Calves/Heifers': 'बछड़ों/हेफर्स की संख्या',
        'No. of Desi Cows': 'देसी गायों की संख्या',
        'No. of Crossbreed Cows': 'क्रॉसब्रीड गायों की संख्या',
        'No. of Buffalo': 'भैंसों की संख्या',
        'Milk Production': 'दूध उत्पादन (लीटर/दिन)',
        'Green Fodder': 'हरा चारा उपलब्ध?',
        'Type of Green Fodder': 'हरे चारे का प्रकार',
        'Quantity of Green Fodder': 'हरे चारे की मात्रा (किलो/दिन)',
        'Dry Fodder': 'सूखा चारा उपलब्ध?',
        'Type of Dry Fodder': 'सूखे चारे का प्रकार',
        'Quantity of Dry Fodder': 'सूखे चारे की मात्रा (किलो/दिन)',
        'Concentrate Feed': 'सांद्रित फ़ीड उपलब्ध?',
        'Brand of Concentrate Feed': 'सांद्रित फ़ीड ब्रांड',
        'Quantity of Concentrate Feed': 'सांद्रित फ़ीड मात्रा (किलो/दिन)',
        'Mineral Mixture': 'खनिज मिश्रण उपलब्ध?',
        'Brand of Mineral Mixture': 'खनिज मिश्रण ब्रांड',
        'Quantity of Mineral Mixture': 'खनिज मिश्रण मात्रा (ग्राम/दिन)',
        'Silage': 'सायलेज उपलब्ध?',
        'Source and Price of Silage': 'सायलेज स्रोत और कीमत',
        'Quantity of Silage': 'सायलेज मात्रा (किलो/दिन)',
        'Source of Water': 'पानी का स्रोत',
        'Submit': 'जमा करें',
        'Download CSV': 'CSV डाउनलोड करें',
        'Select Language': 'भाषा चुनें',
    },
   # Add inside your `translations` dictionary

'Telugu': {
    'Farmer Profile': 'రైతు వివరాలు',
    'Farm Details': 'పశువుల వివరాలు',
    'Specific Questions': 'ప్రత్యేక ప్రశ్నలు',
    'HPC/MCC Name': 'HPC/MCC పేరు',
    'HPC/MCC Code': 'HPC/MCC కోడ్',
    'Type': 'రకం',
    'HPCC': 'HPCC',
    'MCC': 'MCC',
    'Farmer Name': 'రైతు పేరు',
    'Farmer Code': 'రైతు కోడ్ / పౌరర్ ఐడి',
    'Gender': 'లింగం',
    'Male': 'పురుషుడు',
    'Female': 'స్త్రీ',
    'Number of Cows': 'ఆవుల సంఖ్య',
    'No. of Cattle in Milk': 'పాలలో ఉన్న పశువులు',
    'No. of Calves/Heifers': 'దూడలు / హెఫర్ల సంఖ్య',
    'No. of Desi Cows': 'దేశీ ఆవుల సంఖ్య',
    'No. of Crossbreed Cows': 'క్రాస్‌బ్రీడ్ ఆవుల సంఖ్య',
    'No. of Buffalo': 'గేదెల సంఖ్య',
    'Milk Production': 'పాల ఉత్పత్తి (లీటర్లు/రోజు)',
    'Green Fodder': 'పచ్చి మేత అందుబాటులో ఉందా?',
    'Type of Green Fodder': 'పచ్చి మేత రకం',
    'Quantity of Green Fodder': 'పచ్చి మేత పరిమాణం (కిలోలు/రోజు)',
    'Dry Fodder': 'పొడి మేత అందుబాటులో ఉందా?',
    'Type of Dry Fodder': 'పొడి మేత రకం',
    'Quantity of Dry Fodder': 'పొడి మేత పరిమాణం (కిలోలు/రోజు)',
    'Concentrate Feed': 'సాంద్రీకృత ఫీడ్ అందుబాటులో ఉందా?',
    'Brand of Concentrate Feed': 'సాంద్రీకృత ఫీడ్ బ్రాండ్',
    'Quantity of Concentrate Feed': 'సాంద్రీకృత ఫీడ్ పరిమాణం (కిలోలు/రోజు)',
    'Mineral Mixture': 'ఖనిజ మిశ్రమం అందుబాటులో ఉందా?',
    'Brand of Mineral Mixture': 'ఖనిజ మిశ్రమం బ్రాండ్',
    'Quantity of Mineral Mixture': 'ఖనిజ మిశ్రమ పరిమాణం (గ్రాములు/రోజు)',
    'Silage': 'సైలేజ్ అందుబాటులో ఉందా?',
    'Source and Price of Silage': 'సైలేజ్ మూలం మరియు ధర',
    'Quantity of Silage': 'సైలేజ్ పరిమాణం (కిలోలు/రోజు)',
    'Source of Water': 'నీటి మూలం',
    'Submit': 'సమర్పించండి',
    'Download CSV': 'CSV డౌన్లోడ్ చేయండి',
    'Select Language': 'భాషను ఎంచుకోండి'
},

'Marathi': {
    'Farmer Profile': 'शेतकरी माहिती',
    'Farm Details': 'पशुपालन माहिती',
    'Specific Questions': 'विशेष प्रश्न',
    'HPC/MCC Name': 'HPC/MCC नाव',
    'HPC/MCC Code': 'HPC/MCC कोड',
    'Type': 'प्रकार',
    'HPCC': 'HPCC',
    'MCC': 'MCC',
    'Farmer Name': 'शेतकऱ्याचे नाव',
    'Farmer Code': 'शेतकरी कोड / पौरर आयडी',
    'Gender': 'लिंग',
    'Male': 'पुरुष',
    'Female': 'स्त्री',
    'Number of Cows': 'गायींची संख्या',
    'No. of Cattle in Milk': 'दूध देणाऱ्या जनावरांची संख्या',
    'No. of Calves/Heifers': 'वासरांची/कालवडींची संख्या',
    'No. of Desi Cows': 'देशी गायींची संख्या',
    'No. of Crossbreed Cows': 'क्रॉसब्रीड गायींची संख्या',
    'No. of Buffalo': 'म्हशींची संख्या',
    'Milk Production': 'दूध उत्पादन (लिटर/दिवस)',
    'Green Fodder': 'हिरवा चारा उपलब्ध आहे का?',
    'Type of Green Fodder': 'हिरव्या चाऱ्याचा प्रकार',
    'Quantity of Green Fodder': 'हिरव्या चाऱ्याचे प्रमाण (किलो/दिवस)',
    'Dry Fodder': 'कोरडा चारा उपलब्ध आहे का?',
    'Type of Dry Fodder': 'कोरड्या चाऱ्याचा प्रकार',
    'Quantity of Dry Fodder': 'कोरड्या चाऱ्याचे प्रमाण (किलो/दिवस)',
    'Concentrate Feed': 'सांद्रित आहार उपलब्ध आहे का?',
    'Brand of Concentrate Feed': 'सांद्रित आहार ब्रँड',
    'Quantity of Concentrate Feed': 'सांद्रित आहार प्रमाण (किलो/दिवस)',
    'Mineral Mixture': 'खनिज मिश्रण उपलब्ध आहे का?',
    'Brand of Mineral Mixture': 'खनिज मिश्रण ब्रँड',
    'Quantity of Mineral Mixture': 'खनिज मिश्रण प्रमाण (ग्रॅम/दिवस)',
    'Silage': 'सायलेज उपलब्ध आहे का?',
    'Source and Price of Silage': 'सायलेजचा स्रोत व किंमत',
    'Quantity of Silage': 'सायलेज प्रमाण (किलो/दिवस)',
    'Source of Water': 'पाण्याचा स्रोत',
    'Submit': 'सबमिट करा',
    'Download CSV': 'CSV डाउनलोड करा',
    'Select Language': 'भाषा निवडा'
}

    }
}

# 🌟 App Starts Here

st.set_page_config(page_title="Dairy Farmer Survey", page_icon="🐄", layout="centered")

lang = st.selectbox("Select Language / भाषा / భాష / भाषा", ("English", "Hindi", "Telugu", "Marathi"))
labels = translations.get(lang, translations['English'])

st.title(labels['Farmer Profile'])

with st.form("survey_form"):
    # Farmer Profile
    hpc_name = st.text_input(labels['HPC/MCC Name'])
    hpc_code = st.text_input(labels['HPC/MCC Code'])
    type_val = st.selectbox(labels['Type'], (labels['HPCC'], labels['MCC']))
    farmer_name = st.text_input(labels['Farmer Name'])
    farmer_code = st.text_input(labels['Farmer Code'])
    gender = st.selectbox(labels['Gender'], (labels['Male'], labels['Female']))

    st.title(labels['Farm Details'])
    num_cows = st.number_input(labels['Number of Cows'], min_value=0, step=1)
    num_cattle_milk = st.number_input(labels['No. of Cattle in Milk'], min_value=0, step=1)
    num_calves = st.number_input(labels['No. of Calves/Heifers'], min_value=0, step=1)
    num_desi = st.number_input(labels['No. of Desi Cows'], min_value=0, step=1)
    num_cross = st.number_input(labels['No. of Crossbreed Cows'], min_value=0, step=1)
    num_buffalo = st.number_input(labels['No. of Buffalo'], min_value=0, step=1)
    milk_prod = st.number_input(labels['Milk Production'], min_value=0, step=1)

    st.title(labels['Specific Questions'])
    green_fodder = st.selectbox(labels['Green Fodder'], ("Yes", "No"))
    type_green = st.text_input(labels['Type of Green Fodder'])
    qty_green = st.number_input(labels['Quantity of Green Fodder'], min_value=0)

    dry_fodder = st.selectbox(labels['Dry Fodder'], ("Yes", "No"))
    type_dry = st.text_input(labels['Type of Dry Fodder'])
    qty_dry = st.number_input(labels['Quantity of Dry Fodder'], min_value=0)

    concentrate = st.selectbox(labels['Concentrate Feed'], ("Yes", "No"))
    brand_conc = st.text_input(labels['Brand of Concentrate Feed'])
    qty_conc = st.number_input(labels['Quantity of Concentrate Feed'], min_value=0)

    mineral_mix = st.selectbox(labels['Mineral Mixture'], ("Yes", "No"))
    brand_mineral = st.text_input(labels['Brand of Mineral Mixture'])
    qty_mineral = st.number_input(labels['Quantity of Mineral Mixture'], min_value=0)

    silage = st.selectbox(labels['Silage'], ("Yes", "No"))
    source_silage = st.text_input(labels['Source and Price of Silage'])
    qty_silage = st.number_input(labels['Quantity of Silage'], min_value=0)
    source_water = st.text_input(labels['Source of Water'])

    submit = st.form_submit_button(labels['Submit'])

if submit:
    now = datetime.datetime.now()
    data = {
        'Timestamp': [now.isoformat()],
        'Language': [lang],
        'HPC/MCC Name': [hpc_name],
        'HPC/MCC Code': [hpc_code],
        'Type': [type_val],
        'Farmer Name': [farmer_name],
        'Farmer Code': [farmer_code],
        'Gender': [gender],
        'Number of Cows': [num_cows],
        'No. of Cattle in Milk': [num_cattle_milk],
        'No. of Calves/Heifers': [num_calves],
        'No. of Desi Cows': [num_desi],
        'No. of Crossbreed Cows': [num_cross],
        'No. of Buffalo': [num_buffalo],
        'Milk Production (liters/day)': [milk_prod],
        'Green Fodder Available?': [green_fodder],
        'Type of Green Fodder': [type_green],
        'Quantity of Green Fodder (Kg/day)': [qty_green],
        'Dry Fodder Available?': [dry_fodder],
        'Type of Dry Fodder': [type_dry],
        'Quantity of Dry Fodder (Kg/day)': [qty_dry],
        'Concentrate Feed Available?': [concentrate],
        'Brand of Concentrate Feed': [brand_conc],
        'Quantity of Concentrate Feed (Kg/day)': [qty_conc],
        'Mineral Mixture Available?': [mineral_mix],
        'Brand of Mineral Mixture': [brand_mineral],
        'Quantity of Mineral Mixture (gm/day)': [qty_mineral],
        'Silage Available?': [silage],
        'Source and Price of Silage': [source_silage],
        'Quantity of Silage (Kg/day)': [qty_silage],
        'Source of Water': [source_water]
    }
    df = pd.DataFrame(data)

    if os.path.exists("survey_data.csv"):
        df.to_csv("survey_data.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("survey_data.csv", index=False)

    st.success("✅ Survey Saved Successfully!")

# Download Button
if os.path.exists("survey_data.csv"):
    with open("survey_data.csv", "rb") as f:
        st.download_button(
            label=translations[lang]['Download CSV'],
            data=f,
            file_name="survey_data.csv",
            mime="text/csv"
        )
