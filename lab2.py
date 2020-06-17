#Зчитуємо два дійсних числа
x = float(input("Give me the first number: "))
y = float(input("Give me the second number: "))
#Визначаємо максимальний та мінімальний елемент.
mx = max(x,y)
mi = min(x,y)
#Друкуємо відповідь
print("Max of this numbers is: " + str(mx))
print("Min of this numbers is: " + str(mi))