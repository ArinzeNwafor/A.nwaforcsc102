entry = 0
sum1 = 0
print("Enter numbers to find their sum, negative numbers breaks the loop: ")
while True:
    #int() typecasts strings to integer
    entry = int(input())
    if (entry < 0):
        break
    sum1 += entry
print("Sum = ", sum1)