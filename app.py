import streamlit as st
from logic import get_gender_and_country
from faker import Faker

st.title(':earth_americas::man_and_woman_holding_hands: Gender and Country Prediction')

# Create a Faker instance for generating random names
fake = Faker(['fa_IR', 'en_US',"fr_FR", "it_IT", "de_DE", "ar_AE"])

# Add a "Random" button
if st.button("Random"):
    random_name = fake.first_name()
    text_input = st.text_input("Enter a name 👇", value=random_name)
else:
    text_input = st.text_input("Enter a name 👇")

predicted_gender, predicted_country = get_gender_and_country(text_input)
st.write(f"Predicted gender: {predicted_gender}")
st.write(f"Predicted country: {predicted_country}")
