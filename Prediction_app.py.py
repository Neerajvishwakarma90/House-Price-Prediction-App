import pandas as pd
import streamlit as st
import joblib as jb

model = jb.load('model.pkl')

st.header("Banglore House Price Predictor")

data = pd.read_csv(r'C:\college projects\minor project DM\clean_house_data.csv')

loc = st.selectbox("Choose the location ", data['location'].unique())
sqft = st.number_input("Enter Total square feet ")
beds = st.number_input("Enter No of bedrooms ")
bath = st.number_input("Enter No of bathrooms ")
balc = st.number_input("Enter No of balcony's ")

Input = pd.DataFrame([[loc, sqft, bath, balc, beds]],
                     columns=['location', 'total_sqft', 'bath', 'balcony', 'bedroom'])

if st.button("Predict the price"):
    output = model.predict(Input)
    price = output[0] * 100000
    st.write(f"🏠 The price of the house is: ₹ {price:,.2f}")
