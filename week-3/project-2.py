pick = float(input("1. Root of a cubic equation 2. Roots of a quadratic equation: "))

if pick == 2:
    a = float(input("input a: "))
    b = float(input("input b: "))
    c = float(input("input c: "))

    root1 = (-b + (((b ** 2) - 4 * a * c)) ** 0.5) / 2 * a
    root2 = (-b - (((b ** 2) - 4 * a * c)) ** 0.5) / 2 * a

    print(root1)
    print(root2)

elif pick == 1:
    a = float(input("input a: "))
    b = float(input("input b: "))
    c = float(input("input c: "))
    d = float(input("input d: "))

