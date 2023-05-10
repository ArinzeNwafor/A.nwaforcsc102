print("GIRLS")
print("NAME   AGE   HT  SCR")

girls = ['Samantha', 'Jada', 'Jane', 'Claire', 'Elizabeth', 'Mary', 'Susan',
         'Waje', 'Taibat', 'Lilian']

g_age = [17,16,17,18,16,18,17,20,19,17]
g_height = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
g_scores = [80,85,70,60,76,66,87,95,50,49]

for num in range(10):
    print(girls[num], g_age[num], g_height[num], g_scores[num])

print("Boys")
print("NAME   AGE   HT  SCR")
boys = ['Charles', 'Jude', 'James', 'Kelvin', 'Biodun', 'Wale', 'Kunle', 'Matthew', 'Tom', 'Kayode']
b_age = [19,16,18,17,20,19,16,18,17,19]
b_height = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
b_scores = [80,85,70,60,76,66,87,95,50,49]

for i in range(10):
    print(boys[i], b_age[i], b_height[i], b_scores[i])
