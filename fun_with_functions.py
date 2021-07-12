#capitalize all the data that a user enters
#first name
#middle name
#last name
#address
#city
#state
#zipcode

#
first_name = input("Enter your first name please: ")
middle_name = input("Enter your middle name please: ")
last_name = input("Enter your last name please: ")
address = input("Enter your address please: ")
city = input("Enter your city please: ")
state = input("Enter your state please: ")
zipcode = input("Enter your zipcode please: ")
def cap(info):
    print(info.upper())
    print(info.lower())
    print(info)
def complexCapitalize(fn, mn, ln, ad, ct, st, zp):
    cap(fn)
    cap(mn)
    cap(ln)
    cap(ad)
    cap(ct)
    cap(st)
    cap(zp)
complexCapitalize(first_name, middle_name, last_name, address, city, state, zipcode)
