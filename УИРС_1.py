#Нахождение минимума функции методом перебора с уменьшающейся погрешностью

def f(x):
    return(127/4*x**2 - 61/4*x+2)
def MethodWithDecErr(a,b,eps,e):
    currX = a
    currF = min(f(a),f(b))
    res = currF
    resX = currX
    while (eps > e):
        currX = a
        breakpoint()
        while currX <= b:
            currF = f(currX)
            if currF < res:
                res = currF
                resX = currX
            currX += eps
        a = resX - eps
        b = resX + eps
        print("f({0:.4f}) = {1:.4f}".format(resX,res))
        eps /= 2
print("Нахождение минимума функции методом перебора с уменьшающейся погрешностью\n")
print("f(x) = 127/4*x**2 - 61/4*x+2")
print("Введите рассматриваемый отрезок")
a = float(input("a: "))
b = float(input("b: "))
eps = float(input("Введите начальную погрешность: "))
e = float(input("Введите конечную погрешность: "))
MethodWithDecErr(a,b,eps,e)
input()
