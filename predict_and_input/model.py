import joblib


modle = joblib.load("final_praject.pkl")

def predict_price(area, rooms, age):
    prediction = modle.predict([[area, rooms, age]])
    return round(prediction[0])