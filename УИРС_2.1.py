#Нахождение минимума функции методом Фибоначчи

def f(x):
    return(127 / 4 * x**2 - 61 / 4 * x + 2)

#Функция NF возвращает количество N вычислений функции (минимальное натуральное
#число N, для которого 1/F[N] <= e) и список чисел Фибоначчи
def NF(a, b, e):
    F = [1,1]
    N = 1
    while (1/F[N] > e):
        F.append(F[N-1] + F[N])
        N += 1
    return (N + 1,F)

def Fibonacci_method(a,b,e):
    N,F = NF(a, b, e)
    k = 0
    y = a + F[N-2-1] / F[N-1] * (b - a)
    z = a + F[N-1-1] / F[N-1] * (b - a)
    fy = f(y)
    fz = f(z)
    while k != (N-3):
        if fy <= fz:
            b = z
            z = y
            y = a + F[N-k-2-1] / F[N-k-1] * (b - a)
            fz = fy
            fy = f(y)
        else:
            a = y
            y = z
            z = a + F[N-k-1-1] / F[N-k-1] * (b - a)
            fy = fz
            fz = f(z)
        k += 1
    if fy <= fz:
        b = z
    else:
        a = y
    res = (a+b)/2
    return (res, f(res))

print("Нахождение минимума функции методом Фибоначчи\n")
print("f(x) = 127/4*x**2 - 61/4*x+2")
print("Введите рассматриваемый отрезок")
a = float(input("a: "))
b = float(input("b: "))
e = float(input("Введите погрешность e: "))
result = Fibonacci_method(a,b,e)
print(f"f({result[0]:.4f}) = {result[1]:.4f}")
input()
