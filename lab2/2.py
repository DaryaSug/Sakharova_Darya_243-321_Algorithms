a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a <= b and a <= c:
    result = b + c
elif b <= a and b <= c:
    result = a + c
else:
    result = a + b

print("Сумма двух наибольших чисел:", result)
