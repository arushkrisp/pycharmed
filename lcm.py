a = input("First number: ")
b = input("Second number: ")
a = int(a)
b = int(b)
m = []
for i in range(a, a*b, a):
    for j in range(b, a*b, b):
        if i == j:
            m.append(i)
print(m[0])

