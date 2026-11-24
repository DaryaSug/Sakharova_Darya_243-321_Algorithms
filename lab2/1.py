a = int(input("Введите целое число A: "))
b = int(input("Введите целое число B: "))

if a > b:
    b = a
elif b > a:
    a = b
else:
    a = 0
    b = 0

print("Новое значение A:", a)
print("Новое значение B:", b)
