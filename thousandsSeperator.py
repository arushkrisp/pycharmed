userEntered = input("Enter a positive number (big number please): ")
numbers = []
def thousSep(num):
    if int(num) >= 0:
        for i in str(num):
            numbers.append(i)
        numlen = len(numbers)
        numOf3 = int(numlen / 3)
        if i != 0:
            if numlen % 3 == 0:
                for i in range(numlen - 3, numlen - (numOf3 * 3), -3):
                    numbers.insert(i, ",")
            else:
                for i in range(numlen - 3, numlen - (numOf3 * 3) - 1, -3):
                    numbers.insert(i, ",")
        joined = "".join(numbers)
        print(joined)
    else:
        print("Please enter a positive number and try again.")
thousSep(userEntered)