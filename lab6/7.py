# Задание 7. Поменять местами столбцы, содержащие минимум и максимум всей матрицы.
# При повторении значений выбираем первые вхождения при просмотре по строкам.

m = int(input("Введите положительное число строк M: "))  
n = int(input("Введите положительное число столбцов N: "))  
matrix = []  

for i in range(m):  
    row = []  
    for j in range(n):  
        value = float(input(f"Введите A{i + 1},{j + 1}: ")) 
        row.append(value)  
    matrix.append(row) 

minimum = matrix[0][0] 
maximum = matrix[0][0]  
min_column = 0  
max_column = 0  

for i in range(m):  
    for j in range(n):  
        if matrix[i][j] < minimum:  # Проверяем, нашли ли новый минимум всей матрицы.
            minimum = matrix[i][j] 
            min_column = j  
        if matrix[i][j] > maximum:  # Проверяем, нашли ли новый максимум.
            maximum = matrix[i][j]  
            max_column = j  
for row in matrix:  
    row[min_column], row[max_column] = row[max_column], row[min_column]  

print("Преобразованная матрица:") 
for row in matrix:  
    print(*row)  
