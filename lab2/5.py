number = int(input("Введите целое число: "))

if number == 0:
    print("нулевое число")
else:
    if number > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"

    if number % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"

    print(sign, parity, "число")
