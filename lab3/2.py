n = int(input("Введите целое число N больше 0: "))
product = 1

for i in range(1, n + 1):
    factor = 1 + i / 10
    product = product * factor

print("Произведение:", product)
