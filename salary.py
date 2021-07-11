salary = input("Enter your salary: ")
salary = float(salary)
if salary <= 1000:
    print("You need to earn more.")
elif salary < 2000:
    print("You make good money.")
elif salary < 3500:
    print("You lead a luxurious life.")
elif salary <= 5000:
    print("You are a role model.")
else:
    print("You need to start donations.")
if salary <= 2500:
    taxes = 23.35
elif salary <= 5000:
    taxes = 28.55
else:
    taxes = 33.65
totalTaxes = salary * taxes / 100
print("Your taxes are $" + str(totalTaxes))
print("So, you would make $" + str(salary - totalTaxes))