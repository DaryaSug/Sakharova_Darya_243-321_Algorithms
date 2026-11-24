n = int(input("Введите целое число N больше 0: "))
total = 0

for i in range(1, n + 1):
    odd = 2 * i - 1
    total = total + odd
    print("Текущая сумма:", total)

print("Квадрат числа N:", total)
