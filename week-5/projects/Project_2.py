
print(" Annual Tax Revenue Generator ")
experience = float(input("How many years of work experience do you have: "))
age = float(input("Input age: "))

if experience >= 25:
    print("Annual Tax revenue = 5,600,000")

elif experience >= 20 and experience < 25:
    print('Annual Tax revenue = 4,480,000')

elif experience >= 10 and experience < 20:
    print('Annual Tax revenue = 1,150,000')

else:
    print('Annual Tax revenue = 550,000')