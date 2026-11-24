a = float(input("Введите число A: "))
n = int(input("Введите целое число N больше 0: "))
power = 1
total = 1

for i in range(1, n + 1):
    power = power * a
    total = total + power

print("Сумма степеней:", total)
