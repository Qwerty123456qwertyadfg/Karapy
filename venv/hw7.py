import math
how = int(input(" 1 - прямоугольник , 2 - треугольник , 3 - круг"))
def col (a,b):

        print(s)

if how == 1:
        a = int(input("Ширина"))
        b = int(input("Высота"))
        s = a * b


if how == 2:
        a = int(input("Ocнование"))
        b = int(input("Высота"))
        s = (a*b) /2

if how == 3:
        a = int(input("Радиус"))
        b = math.pi
        s = (a**2)*b

print(s)
