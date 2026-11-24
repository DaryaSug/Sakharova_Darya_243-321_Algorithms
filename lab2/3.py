from math import sqrt

ax = float(input("Введите x точки A: "))
ay = float(input("Введите y точки A: "))
bx = float(input("Введите x точки B: "))
by = float(input("Введите y точки B: "))
cx = float(input("Введите x точки C: "))
cy = float(input("Введите y точки C: "))

ab = sqrt((bx - ax) ** 2 + (by - ay) ** 2)
ac = sqrt((cx - ax) ** 2 + (cy - ay) ** 2)

if ab < ac:
    print("Ближе точка B с координатами:", bx, by)
    print("Расстояние от A:", ab)
elif ac < ab:
    print("Ближе точка C с координатами:", cx, cy)
    print("Расстояние от A:", ac)
else:
    print("Точки B и C находятся на одинаковом расстоянии от A.")
    print("Координаты B:", bx, by)
    print("Координаты C:", cx, cy)
    print("Расстояние от A:", ab)
