number = int(input("Введите целое число от 1 до 999: "))

if number < 1 or number > 999:
    print("Нужно ввести число от 1 до 999.")
else:
    if number % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"

    if number < 10:
        digits = "однозначное"
    elif number < 100:
        digits = "двузначное"
    else:
        digits = "трехзначное"

    print(parity, digits, "число")
