# Задание 8. В матрице с чётными M и N поменять местами левую верхнюю и правую нижнюю четверти.

m = int(input("Введите положительное чётное число строк M: "))  
n = int(input("Введите положительное чётное число столбцов N: "))  

if m <= 0 or n <= 0 or m % 2 != 0 or n % 2 != 0:  
    print("Оба размера матрицы должны быть положительными чётными числами.")  
else:  
    matrix = []  
    for i in range(m):  
        row = [] 
        for j in range(n):  
            value = float(input(f"Введите A{i + 1},{j + 1}: ")) 
            row.append(value) 
        matrix.append(row)  

    half_rows = m // 2  # Половина строк — высота одной четверти.
    half_columns = n // 2  # Половина столбцов — ширина одной четверти.

    for i in range(half_rows):  
        for j in range(half_columns):  
            matrix[i][j], matrix[i + half_rows][j + half_columns] = matrix[i + half_rows][j + half_columns], matrix[i][j]  

    print("Преобразованная матрица:")  
    for row in matrix:  
        print(*row)  
