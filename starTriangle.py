numRows = input("How many rows? Enter here: ")
numRows = int(numRows)
numOfStars = []
def starTriangle(rows):
    for i in range(1, rows + 1, 1):
        numOfStars.append(int((i * 2) - 1))
    for num in numOfStars:
        if numRows % 2 == 0:
            greatestNum = numOfStars[len(numOfStars) - int(numRows / 2)]
        else:
            greatestNum = numOfStars[len(numOfStars) - int((numRows / 2) + 0.5)]
        stars = num * "*"
        numSpaces = int(greatestNum - (num / 2))
        spaces = numSpaces * " "
        starRow = (spaces + stars + spaces)
        print(starRow)
starTriangle(numRows)