userName1 = input("Please enter your first name: ")
print("first name: ", userName1)
userName2 = input("Please enter your last name: ")
print("last name: ", userName2)
print("Welcome,", userName1, userName2)

n = input("Please enter your hourly rate: ")
print("hourly rate: ", n)
m = input("Please enter your total working hours: ")
print("total working hours: ", m)
product1 = float(n) * float(m)
print("Gross pay: ", format(product1))

a = input("How was the user experience (1-10)? ")
b = input("How was the connectivity (1-10)? ")
c = input("How was the speed (1-10)? ")
product2 = (float(a) + float(b) + float(c)) / 3
print("Overall Experience Average: ", format(product2))

if product2 <= 3:
    print("Overall Experience: ", "Not Satisfied")
elif product2 >= 4  <= 6:
    print("Overall Experience: ", "Somewhat Satisfied")
elif product2 >= 6  <= 8:
    print("Overall Experience: ", "Satisfied")
elif product2 >= 8:
    print("Overall Experience: ", "Very Satisfied")