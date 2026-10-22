import joblib


modle = joblib.load("train_model/final_praject.pkl")

def predict_price(area, rooms, age):
    prediction = modle.predict([[area, rooms, age]])
    return round(prediction[0])