import streamlit as st
import pandas as pd

from log.log_confing import logger
import train_model.final_praject as final_praject
from predict_and_input.model import predict_price

st.title("🏠 House Price Prediction")

st.write("Compare the predicted prices of three houses.")

st.divider()

st.subheader("🏡 House Details")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("House 1")
    area1 = st.number_input("Area 1 (m²)", min_value=1.0, value=80.0)
    rooms1 = st.number_input("Rooms 1", min_value=1, value=2, step=1)
    age1 = st.number_input("Age 1", min_value=0, value=10, step=1)

with col2:
    st.write("House 2")
    area2 = st.number_input("Area 2 (m²)", min_value=1.0, value=120.0)
    rooms2 = st.number_input("Rooms 2", min_value=1, value=3, step=1)
    age2 = st.number_input("Age 2", min_value=0, value=5, step=1)

with col3:
    st.write("House 3")
    area3 = st.number_input("Area 3 (m²)", min_value=1.0, value=150.0)
    rooms3 = st.number_input("Rooms 3", min_value=1, value=4, step=1)
    age3 = st.number_input("Age 3", min_value=0, value=2, step=1)

st.divider()

st.subheader("📊 Model Performance")

col1, col2 = st.columns(2)
col1.metric("R² Score", f"{final_praject.r2:.4f}")
col2.metric("Mean Absolute Error", f"{final_praject.mea:,.2f}")

if st.button("Compare Houses"):
    houses = [
        ("House 1", area1, rooms1, age1),
        ("House 2", area2, rooms2, age2),
        ("House 3", area3, rooms3, age3),
    ]

    results = []

    for name, area, rooms, age in houses:
        prediction = predict_price(area, rooms, age)

        results.append({
            "House": name,
            "Area (m²)": area,
            "Rooms": rooms,
            "Age": age,
            "Predicted Price": prediction
        })

    df = pd.DataFrame(results)

    st.subheader("📋 Comparison Results")
    st.dataframe(df, hide_index=True)

    best_house = max(results, key=lambda house: house["Predicted Price"])

    st.success(
        f'{best_house["House"]} has the highest predicted price: '
        f'{best_house["Predicted Price"]:,}'
    )

    logger.info("House comparison completed")