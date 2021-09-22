nterm = input("The number of terms: ")
nterm = int(nterm)
n1, n2 = 0, 1
if nterm <= 0:
    print("Positive number please")
elif nterm == 1:
    print(n1)
else:
    for n in range (0, nterm, 1):
        print(n1)
        next = n1 + n2
        n1 = n2
        n2 = next