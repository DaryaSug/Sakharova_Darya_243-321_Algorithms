a = int(input("Введите положительное целое число A: "))
b = int(input("Введите положительное целое число B: "))

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("Наибольший общий делитель:", a)
