fac = input("Your number: ")
fac = int(fac)
facs = []
for i in range(1, fac, 1):
    if fac % i == 0:
        ans = fac / i
        facs.append(int(ans))
facs.append(1)
print(facs)
if facs.index(1) == 1 or facs.index(1) == 0:
    print("That is a prime number")
else:
    print("That is a composite number")