a = int(input("Введите положительное целое число A: "))
b = int(input("Введите положительное целое число B больше A: "))

for number in range(a, b + 1):
    for repeat in range(number):
        print(number)
