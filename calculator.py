sign = input("What sign will you use? Enter here: ")
if (sign.lower() == "multiplication" or sign.lower() == "division" or sign.lower() == "addition" or sign.lower() == "subtraction"):
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")
    num1, num2 = int(num1), int(num2)
    if (sign.lower() == "multiplication"):
        answer = num1 * num2
        sign = "*"
    elif (sign.lower() == "division"):
        answer = num1 / num2
        if answer % 1 == 0.0:
            answer = int(answer)
        else:
            pass
        sign = "/"
    elif (sign.lower() == "addition"):
        answer = num1 + num2
        sign = "+"
    elif (sign.lower() == "subtraction"):
        answer = num1 - num2
        sign = "-"
    
    num1, num2, answer = str(num1), str(num2), str(answer)
    print("The answer is " + num1 + " " + sign + " " + num2 + " = " + answer)
else:
    print("That is not a sign.")