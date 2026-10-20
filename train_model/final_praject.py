from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd
import joblib
from log.log_confing import logger

data = pd.read_csv("data/final_praject.csv")

X = data[['area', 'rooms', 'age']]
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size=0.2, random_state=42)

modle = LinearRegression()
logger.info("Model training started")
modle.fit(X_train, y_train)

pre = modle.predict(X_test)

r2 = r2_score(y_test, pre)
mea = mean_absolute_error(y_test, pre)

print("r2 : ", r2)
print("mea : ", mea)

# print(modle.predict([[100, 2, 2]])[0])



# area = float(input("Enter your house area:"))
# rooms = int(input("Enter your house rooms:"))
# age = int(input("Enter your house age:"))


# modle = joblib.load("final_praject.pkl")

# prediction = modle.predict([[area, rooms, age]])

# print("Predicted price:", round(prediction[0]))


joblib.dump(modle, "final_praject.pkl")
logger.success("Model saved successfully")