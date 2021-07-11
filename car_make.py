#Get their first make of the car
car = input("Enter the first make of your car: ")
lowerCar = car.lower()
if (lowerCar == "bmw" or lowerCar == "audi" or lowerCar == "mercedes"):
    print("You like German cars.")
elif (lowerCar == "ford" or lowerCar == "gm" or lowerCar == "tesla"):
    print("You are a core American.")
elif (lowerCar == "ferrari"):
    print("You like Italian cars.")
elif (lowerCar == "honda" or lowerCar == "toyota" or lowerCar == "nissan" or lowerCar == "subaru"):
    print("You like Japenese cars.")
elif (lowerCar == "jaguar" or lowerCar == "land rover"):
    print("You like Indian cars.")
elif (car == " " or car == "" or lowerCar == "none"):
    print("You have lots of choices to pick from.")
else:
    print("Sorry, that is not a car make.")