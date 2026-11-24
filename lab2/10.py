year = int(input("Введите год: "))

cycle_year = (year - 1984) % 60
color_number = cycle_year // 12
animal_number = cycle_year % 12

animals = ("крысы", "коровы", "тигра", "зайца", "дракона", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи")
masculine_colors = ("зеленого", "красного", "желтого", "белого", "черного")
feminine_colors = ("зеленой", "красной", "желтой", "белой", "черной")

if animal_number == 2 or animal_number == 3 or animal_number == 4:
    color = masculine_colors[color_number]
else:
    color = feminine_colors[color_number]

print("год", color, animals[animal_number])
