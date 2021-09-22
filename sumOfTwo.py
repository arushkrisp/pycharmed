fir = [1,9,35,68,5]
sec = [46,687,36,3,8]
solo = 689
sums = []
def sumOfTwo(a, b, v):
    isItPoss = "false"
    for i in a:
        for j in b:
            sum = i + j
            sums.append(sum)
    for i in sums:
        if i == solo:
            isItPoss = "true"
    print(isItPoss)
sumOfTwo(fir, sec, solo)