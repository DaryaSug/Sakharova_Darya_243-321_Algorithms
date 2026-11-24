# Задание 6. В каждой строке поменять местами минимальный и максимальный элементы.
# При повторениях выбираем первое вхождение минимума и первое вхождение максимума в строке.

m = int(input("Введите положительное число строк M: "))  
n = int(input("Введите положительное число столбцов N: "))  
matrix = []  

for i in range(m):  
    row = []  
    for j in range(n):  
        value = float(input(f"Введите A{i + 1},{j + 1}: ")) 
        row.append(value) 
    matrix.append(row)  

for row in matrix:  # Преобразуем каждую строку отдельно.
    min_index = 0  
    max_index = 0  
    for j in range(1, n):  
        if row[j] < row[min_index]:  # Проверяем, найдено ли меньшее значение.
            min_index = j  
        if row[j] > row[max_index]:  # Проверяем, найдено ли большее значение.
            max_index = j  
    row[min_index], row[max_index] = row[max_index], row[min_index]  
print("Преобразованная матрица:")  
for row in matrix:  
    print(*row)  