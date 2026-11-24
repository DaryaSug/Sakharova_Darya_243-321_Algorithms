from decimal import Decimal

a = Decimal(input("Введите положительную длину A: "))
b = Decimal(input("Введите положительную длину B меньше A: "))
remainder = a

while remainder >= b:
    remainder = remainder - b

print("Длина незанятой части:", remainder)
