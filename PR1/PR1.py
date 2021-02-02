#Задание 1
a = 5
b = 10
a += b
b = a - b
a -= b
print(a,b)

#Задание 2
c=0
d = int(input())
while d > 0:
    c += d % 10 
    d //= 10
print(c)

#Задание 3
print("Введите коэффициенты ")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b ** 2 - 4 * a * c
print("D = %.2f" % D)

if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif D == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
