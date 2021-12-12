name = input("PLEASE ENTER YOUR NAME: ")
name = name.upper()
print(name)
age = int(input("PLEASE ENTER YOUR AGE: "))
print(age)
number_hours = float(input("PLEASE ENTER THE NUMBER OF HOURS WORKED: "))
print(number_hours)
number_children = int(input("PLEASE ENTER THE NUMBER OF CHILDREN YOU HAVE: "))
print(number_children)
gender = input("PLEASE ENTER YOUR GENDER: ")
print(gender)
if (gender == 'm' or gender == 'M' and number_children > 3):
    if (number_hours <= 40):
        gross_pay = number_hours * 500
        edu_fund = (number_children - 3) * 10
    else:
        gross_pay = number_hours * 500 + (number_hours - 40) * 1.5
elif (gender == 'f' or gender == 'F' and number_children > 3):
        edu_fund = (number_children - 3) * 10
    if (number_hours <= 40):
        gross_pay = number_hours * 550
        edu_fund = (number_children - 3) * 20
    else:
        gross_pay = number_hours * 40 + (number_hours - 40) * 1.5
        edu_fund = (number_children - 3) * 20
else:
    print("!!!ERROR WITH GENDER ENTER!!!")
income_tax = gross_pay * 0.15
nhcl = gross_pay * 0.25
district_tax = gross_pay * 0.01
total_tax = income_tax + nhcl + edu_fund + district_tax
net_pay = gross_pay - total_tax
print("THE NETPAY OF ", name, " is ", net_pay)
