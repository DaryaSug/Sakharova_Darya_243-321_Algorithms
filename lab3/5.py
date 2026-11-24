a = float(input("Введите число A: "))
n = int(input("Введите целое число N больше 0: "))
term = 1
total = 1

for i in range(1, n + 1):
    term = term * (-a)
    total = total + term

print("Значение выражения:", total)
