# Задание 10. В целочисленном массиве ровно два одинаковых элемента.
# Найти их номера и вывести по возрастанию; номера начинаются с 1.

n = int(input("Введите размер массива N не меньше 2: ")) 
a = []  

for i in range(n): 
    value = int(input(f"Введите целый элемент A{i + 1}: ")) 
    a.append(value) 

found = False  
for i in range(n - 1):  
    for j in range(i + 1, n):  
        if a[i] == a[j]:  
            print("Номера одинаковых элементов:", i + 1, j + 1)  
            found = True  
            break 
    if found:  
        break 

if not found: 
    print("Одинаковых элементов не найдено.")  
