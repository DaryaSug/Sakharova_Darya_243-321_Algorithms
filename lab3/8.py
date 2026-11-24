n = int(input("Введите целое число N больше 1: "))
k = 0
total = 0

while total < n:
    k = k + 1
    total = total + k

print("Наименьшее K:", k)
print("Сумма:", total)
