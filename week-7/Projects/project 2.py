print('Welcome To Yega Services')
print("Delivery service to Ibeju-lekki community and Epe")

weight = float(input("Input weight of the package: "))
location = input("Input destination: ")

if weight < 10 and location == str.casefold('Epe'):
    print("Price of delivery = #4000")

elif weight < 10 and location == str.casefold('Ibeju-Lekki'):
    print("Price of delivery = #1500")

elif weight >= 10 and location == str.casefold('Ibeju-Lekki'):
    print("Price of delivery = #2000")

elif weight >= 10 and location == str.casefold('Epe'):
    print("Price of delivery = #5000")

else:
    print("Delivery to only Ibeju-Lekki and Epe")