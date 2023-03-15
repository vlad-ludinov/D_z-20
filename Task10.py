from random import randint
numberCoins = int(input("Введите количество монеток на столе: "))

orel = 0
reshka  = 0
for i in range(numberCoins):
    side = randint(0,1)
    if side == 0:
        orel +=1
    else:
        reshka +=1
if orel == 0 or reshka == 0:
    print(f"{orel} монет - орел и {reshka} монет - решка")
    print("Все монеты лежат одной стороной")
elif orel < reshka:
    print(f"{orel} монет - орел и {reshka} монет - решка")
    print(f"Нужно перевернуть {orel} монет чтобы все монеты лежали одной стороной")
else:
    print(f"{orel} монет - орел и {reshka} монет - решка")
    print(f"Нужно перевернуть {reshka} монет чтобы все монеты лежали одной стороной")