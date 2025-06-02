
import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter you height (in cm):", 100,250,175)
weight = st.slider("Enter your weight  (in kg):",40,200,70 )

bmi = weight /((height/100)**2)

st.write(f"Your BMI is {bmi:.2f}")
st.write("### BMI Categories ###")
st.write("- Underwieght: BMI less than 18.5")
st.write("- Normal Weight: BMI between 18.5 and 24.5")
st.write("- Obesity: 30 or greater.")