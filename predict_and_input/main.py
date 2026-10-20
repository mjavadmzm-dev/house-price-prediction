from predict_and_input.model import predict_price
import train_model.final_praject as final_praject


try:
    area = float(input("Enter your house area:"))
    rooms = int(input("Enter your house rooms:"))
    age = int(input("Enter your house age:"))


    prediction = predict_price(area, rooms, age)

    print("Predicted price:",  prediction)
except ValueError:
    print("Pleas enter valid number.")