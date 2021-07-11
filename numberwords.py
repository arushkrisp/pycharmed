num = input("Enter your two digit or one digit number: ")
num = int(num)
less_than_20 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ones_place = num % 10
tens_place = int((num - ones_place) / 10)
def num_to_words(number):
    if (num >= 100):
        print("Sorry, that is not a two digit number.")
    elif num == 0:
        print("Your number is zero.")
    else:
        if num < 20:
            message1 = less_than_20[num]
            print("Your number is " + message1 + ".")
        else:
            message1 = tens[tens_place]
            message2 = less_than_20[ones_place]
            if ones_place == 0:
                print("Your number is " + message1 + ".")
            else:
                print("Your number is " + message1 + " " + message2 + ".")
num_to_words(num)