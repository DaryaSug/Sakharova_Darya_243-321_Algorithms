# Задание 3. Найти столбец с наименьшим произведением элементов и вывести его номер и произведение.
# Если наименьшее произведение одинаково у нескольких столбцов, выбираем первый.

m = int(input("Введите положительное число строк M: "))  
n = int(input("Введите положительное число столбцов N: "))  
matrix = []  

for i in range(m):  
    row = []  
    for j in range(n): 
        value = float(input(f"Введите A{i + 1},{j + 1}: "))  
        row.append(value)  # Добавляем число в строку.
    matrix.append(row)  # Сохраняем готовую строку в матрице.

minimum_product = None  # Пока минимальное произведение неизвестно.
column_number = 0  # Здесь сохраним номер подходящего столбца.

for j in range(n):  
    product = 1 
    for i in range(m):  
        product = product * matrix[i][j]  # Умножаем результат на очередной элемент столбца.
    if minimum_product is None or product < minimum_product:  # Первый результат запоминаем сразу, остальные сравниваем с ним.
        minimum_product = product  
        column_number = j + 1  

print("Номер столбца:", column_number)  
print("Наименьшее произведение:", minimum_product)  
