number = int(input("Введите число n: "))

pairs = 0
degree = 0
while pairs*4 <= number:
    pairs = 2**degree
    print(pairs, end = ", ")
    degree+=1
print(pairs*2)