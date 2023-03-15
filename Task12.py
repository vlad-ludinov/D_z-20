productOfNumber = int(input("Введите произведение чисел:"))
sumOfNumber = int(input("Введите сумму чисел"))

discremenant = sumOfNumber**2 - (4 * -1 * -productOfNumber)
x1 = (-sumOfNumber + discremenant**0.5)/(2*-1)
x2 = (-sumOfNumber - discremenant**0.5)/(2*-1)
y1 = sumOfNumber - x1
y2 = sumOfNumber - x2
print(f"x = {round(x1, 3)}, y = {round(y1, 3)}, либо x = {round(x2, 3)}, y = {round(y2, 3)}")

