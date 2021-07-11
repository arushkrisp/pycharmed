import math
num = float(input("Enter your two digit or one digit decimal: "))
less_than_20 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["zero", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundredths_place = int(round((num % 0.1) * 100))
tenths_place = int(round((((num % 1) - (hundredths_place / 100)) * 10)))
ones_place = int(round((num % 10 - ((tenths_place / 10) + (hundredths_place / 100)))))
tens_place = int(round((num % 100 - (ones_place + (tenths_place / 10) + (hundredths_place / 100))) / 10))
hundreds_place = int(round(num - (ones_place + (tenths_place / 10) + (hundredths_place / 100))) / 100)
if hundredths_place > 9:
    hundredths_place = 0
    tenths_place = tenths_place + 1
if (num > 999):
    print("Sorry, that is not a three digit number")
elif num == 0:
    print("Your number is zero.")
else:
    message1 = less_than_20[hundreds_place]
    message2 = tens[tens_place]
    message3 = less_than_20[ones_place]
    message4 = tens[tenths_place]
    message5 = less_than_20[hundredths_place]
    if ((tens_place * 10) + ones_place) < 20:
        message1 = less_than_20[hundreds_place]
        message2 = less_than_20[(tens_place * 10) + ones_place]
        message3 = tens[tenths_place]
        message4 = less_than_20[hundredths_place]
        if ((tenths_place * 10) + hundredths_place) < 20:
            message3 = less_than_20[(tenths_place * 10) + hundredths_place]
            print("Your number is " + message1 + " hundred " + message2 + " dollars and " + message3 + " cents")
        else:
            print("Your number is " + message1 + " hundred " + message2 + " dollars and " + message3 + " " + message4 + " cents")
    elif ((tenths_place * 10) + hundredths_place) < 20:
        message4 = less_than_20[(tenths_place * 10) + hundredths_place]
        print("Your number is " + message1 + " hundred " + message2 + " " + message3 + " dollars and " + message4 + " cents")
    else:
        message1 = less_than_20[hundreds_place]
        message2 = tens[tens_place]
        message3 = less_than_20[ones_place]
        message4 = tens[tenths_place]
        message5 = less_than_20[hundredths_place]
        print("Your number is " + message1 + " hundred " + message2 + " " + message3 + " dollars and " + message4 + " " + message5 + " cents")