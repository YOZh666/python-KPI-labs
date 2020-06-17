#Зчитуємо рядок
s = str(input("Input a string: "))
#Підраховуємо кількість зустрічей aba та abc
abc = s.count('abc')
aba = s.count('aba')
#Виводимо результат
print("abc occur in this text for " + str(abc) + " times.")
print("aba occur in this text for " + str(aba) + " times.")