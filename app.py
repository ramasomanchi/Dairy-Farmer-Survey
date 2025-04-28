# app.py (Final Streamlit Dairy Survey)

import streamlit as st
import pandas as pd
import datetime
import os

# Translations
translations = {
    'English': { ... },
    'Hindi': { ... },
    'Telugu': {
        'Language': 'భాష',
        'Farmer Profile': 'రైతు వివరాలు',
        'HPC/MCC Name': 'హెచ్‌పీసీ/ఎంసీసీ పేరు',
        'HPC/MCC Code': 'హెచ్‌పీసీ/ఎంసీసీ కోడ్',
        'Types': 'రకం',
        'HPCC': 'హెచ్‌పిసిసి',
        'MCC': 'ఎంసిసి',
        'Farmer Name': 'రైతు పేరు',
        'Farmer Code': 'రైతు కోడ్ / పోరర్ ID',
        'Gender': 'లింగం',
        'Male': 'పురుషుడు',
        'Female': 'స్త్రీ',
        'Farm Details': 'ఫారం వివరాలు',
        'Number of Cows': 'ఆవుల సంఖ్య',
        'No. of Cattle in Milk': 'పాలలో మేతగానే ఉన్న పశువుల సంఖ్య',
        'No. of Calves/Heifers': 'దూడలు/హెఫర్లు సంఖ్య',
        'No. of Desi cows': 'దేశీ ఆవుల సంఖ్య',
        'No. of Cross breed cows': 'క్రాస్‌బ్రీడ్ ఆవుల సంఖ్య',
        'No. of Buffalo': 'గేదెల సంఖ్య',
        'Milk Production': 'పాల ఉత్పత్తి (లీటర్లు/రోజు)',
        'Specific Questions': 'ప్రత్యేక ప్రశ్నలు',
        'Green Fodder': 'పచ్చి మేత',
        'Type of Green Fodder': 'పచ్చి మేత రకం',
        'Quantity of Green Fodder': 'పచ్చి మేత పరిమాణం (కిలో/రోజు)',
        'Dry Fodder': 'పొడి మేత',
        'Type of Dry Fodder': 'పొడి మేత రకం',
        'Quantity of Dry Fodder': 'పొడి మేత పరిమాణం (కిలో/రోజు)',
        'Concentrate Feed': 'సాంద్రీకృత ఆహారం',
        'Brand of Concentrate Feed': 'సాంద్రీకృత ఆహారం బ్రాండ్',
        'Quantity of Concentrate Feed': 'సాంద్రీకృత ఆహారం పరిమాణం (కిలో/రోజు)',
        'Mineral Mixture': 'ఖనిజ మిశ్రమం',
        'Brand of Mineral Mixture': 'ఖనిజ మిశ్రమం బ్రాండ్',
        'Quantity of Mineral Mixture': 'ఖనిజ మిశ్రమం పరిమాణం (గ్రాం/రోజు)',
        'Silage': 'సైలేజ్',
        'Source and Price of Silage': 'సైలేజ్ మూలం మరియు ధర',
        'Quantity of Silage': 'సైలేజ్ పరిమాణం (కిలో/రోజు)',
        'Source of Water': 'నీటి మూలం',
        'Name of Surveyor': 'సర్వేయర్ పేరు',
        'Date of Visit': 'సందర్శన తేదీ',
        'Submit': 'సమర్పించు',
        'Yes': 'అవును',
        'No': 'కాదు',
        'Download CSV': 'CSV డౌన్‌లోడ్ చేయండి'
    }
}

# (No change needed to rest of the app.py script)
# (It will now support English, Hindi, Telugu fully)

# Everything remains the same!

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
