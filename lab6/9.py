# Задание 9. Упорядочить строки по возрастанию их первых элементов.
# При одинаковых первых элементах сохраняем исходный порядок соответствующих строк.

m = int(input("Введите положительное число строк M: "))  
n = int(input("Введите положительное число столбцов N: "))  
matrix = []  

for i in range(m):  
    row = [] 
    for j in range(n):  
        value = float(input(f"Введите A{i + 1},{j + 1}: "))  
        row.append(value) 
    matrix.append(row)  

for i in range(m - 1):  # Делаем проходы сортировки пузырьком.
    for j in range(m - 1 - i):  # Сравниваем соседние строки в ещё не отсортированной части.
        if matrix[j][0] > matrix[j + 1][0]:  
            matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j] 

print("Матрица после упорядочивания строк:")  
for row in matrix:  
    print(*row)  
