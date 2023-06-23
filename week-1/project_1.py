pick = float(input("Calculator for 1.Simple Interest 2.Compound interest 3.Annuity plan: "))

if pick == 1:
    P = float(input("Input Principal: "))
    R = float(input("Input the Rate: "))
    T = float(input("Input the Time: "))
    A = (P * R * T) / 100
    print("Amount = ", A)

elif pick == 2:
    P = float(input("Input Principal: "))
    R = float(input("Input the Rate: "))
    T = float(input("Input the Time: "))
    n = float(input("input n: "))
    C = P * (1 + R / n) ** n * T
    print("Compound Interest = ", C)

elif pick == 3:
    P = float(input("Input Principal: "))
    R = float(input("Input the Rate: "))
    T = float(input("Input the Time: "))
    n = float(input("input n: "))
    Annuity_plan = P * (((1 + R / n) ** n * T) - 1) / (R / n)
    print("Annuity plan = ", Annuity_plan)

else:
    print("Invalid input")

