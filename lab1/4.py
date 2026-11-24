# Задание 4. Даны два ненулевых числа.
# Найти сумму, разность, произведение и частное их квадратов.

a = float(input("Введите ненулевое число a: "))  
b = float(input("Введите ненулевое число b: "))  

a_squared = a ** 2  
b_squared = b ** 2  # ** обозначает возведение в степень.

print("Сумма квадратов:", a_squared + b_squared)  
print("Разность квадратов:", a_squared - b_squared)  
print("Произведение квадратов:", a_squared * b_squared)  
print("Частное квадратов:", a_squared / b_squared)  
