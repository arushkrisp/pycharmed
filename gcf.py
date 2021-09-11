a = input("First number: ")
b = input("Second number: ")
a = int(a)
b = int(b)
facsA = []
facsB = []
cmnfacs = []
if a <= 0 or b <= 0:
    print("Please enter a positive number.")
else:
    for i in range(1, a, 1):
        if a % i == 0:
            ansA = a / i
            facsA.append(int(ansA))
    for i in range(1, b, 1):
        if b % i == 0:
            ansB = b / i
            facsB.append(int(ansB))
    facsA.append(1)
    facsB.append(1)
    for i in range(0, len(facsA) - 1, 1):
        for j in range(0, len(facsB) - 1, 1):
            if (facsA[i] == facsB[j]):
                cmnfacs.append(facsA[i])
    cmnfacs.append(1)
    gcf = cmnfacs[0]
    print(gcf)

