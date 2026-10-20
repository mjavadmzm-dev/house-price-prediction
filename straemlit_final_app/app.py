import streamlit as st
from log.log_confing import logger

import train_model.final_praject as final_praject
from predict_and_input.model import predict_price

st.title("House Price Prediction")

st.write("Enter the details of the house.")

area = st.number_input("Area", value=100.0)
rooms = st.number_input("Rooms", value=3, step=1)
age = st.number_input("Age", value=5, step=1)

st.subheader("Model Performance")

st.write("R2:", final_praject.r2)
st.write("Mean Absolute Error:", final_praject.mea)

if st.button("Predict Price"):
    logger.info("Prediction requested")

    prediction = predict_price(area, rooms, age)

    st.success("Predicted price: " + str(prediction))

    logger.success("Prediction completed")