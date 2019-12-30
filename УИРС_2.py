#Нахождение минимума функции методом золотого сечения
def f(x):
    return(127 / 4 * x**2 - 61 / 4 * x + 2)

def G_Section(a, b, e):
    k = (5**(1 / 2) + 1) / 2
    z = a + abs(b - a) * (k - 1)
    y = b - abs(b - a) * (k - 1)
    fy = f(y)
    fz = f(z)
    while abs(b - a) > e:
        if (fz > fy):
            b = z
            z = y
            y = b - abs(b - a) * (k - 1)
            fz = fy
            fy = f(y)
        else:
            a = y
            y = z
            z = a + abs(b - a) * (k - 1)
            fy = fz
            fz = f(z)
    res = min(fy,fz)
    print(("f(a) = f({0:.4f}) = {1:.4f};\nf(b) = f({2:.4f}) = {3:.4f};\nmin = {4:.4f}").format(a, f(a), b, f(b), res))

print("Нахождение минимума функции методом золотого сечения\n")
print("f(x) = 127/4*x**2 - 61/4*x+2")
print("Введите рассматриваемый отрезок")
a = float(input("a: "))
b = float(input("b: "))
e = float(input("Введите погрешность: "))
G_Section(a, b, e)
input()
