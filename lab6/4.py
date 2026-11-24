# Задание 4. В каждом столбце посчитать элементы, которые строго больше среднего этого столбца.

m = int(input("Введите положительное число строк M: "))  
n = int(input("Введите положительное число столбцов N: "))  
matrix = []  

for i in range(m): 
    row = []  
    for j in range(n):  
        value = float(input(f"Введите A{i + 1},{j + 1}: "))  
        row.append(value)  
    matrix.append(row) 

for j in range(n): 
    total = 0  
    for i in range(m): 
        total = total + matrix[i][j]  # Прибавляем очередной элемент к сумме.
    average = total / m  # Делим сумму на число строк и получаем среднее столбца.
    count = 0  
    for i in range(m):  
        if matrix[i][j] > average:  # Сравниваем элемент со средним именно его столбца.
            count = count + 1  # Увеличиваем счётчик подходящих элементов.
    print(f"Столбец {j + 1}, количество элементов больше среднего:", count) 
