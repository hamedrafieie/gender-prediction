from logic import get_gender_and_country
from matplotlib.pyplot import text
import streamlit as st


st.title(':earth_americas::man_and_woman_holding_hands: Gender and county prediction')

option = st.toggle("Random")

text_input = st.text_input("Enter a name 👇")
predicted_gender, predicted_country = get_gender_and_country(text_input)

st.write(f"Predicted gender: ```{predicted_gender}```")
st.write(f"Predicted country: ```{predicted_country}```")