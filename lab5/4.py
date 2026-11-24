# Задание 4. Вывести элементы в порядке: A1, AN, A2, A(N-1) и так далее.
# Если размер нечётный, средний элемент выводится один раз.

n = int(input("Введите положительный размер массива N: "))  
a = []  

for i in range(n):  
    value = float(input(f"Введите элемент A{i + 1}: "))  
    a.append(value)  

result = []  
left = 0  
right = n - 1  

while left <= right:  
    result.append(a[left])  
    if left < right:  
        result.append(a[right])  
    left = left + 1  
    right = right - 1  

print("Элементы в нужном порядке:", result)  
