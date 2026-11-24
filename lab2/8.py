number = int(input("Введите количество заданий от 10 до 40: "))

teens = ("десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать")
units = ("", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять")

if number < 10 or number > 40:
    print("Нужно ввести число от 10 до 40.")
else:
    if number < 20:
        number_text = teens[number - 10]
    else:
        if number < 30:
            number_text = "двадцать"
        elif number < 40:
            number_text = "тридцать"
        else:
            number_text = "сорок"

        if number % 10 != 0:
            number_text = number_text + " " + units[number % 10]

    last_digit = number % 10
    if 11 <= number <= 14:
        ending = "учебных заданий"
    elif last_digit == 1:
        ending = "учебное задание"
    elif 2 <= last_digit <= 4:
        ending = "учебных задания"
    else:
        ending = "учебных заданий"

    print(number_text, ending)
