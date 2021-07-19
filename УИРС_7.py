import math
def half_division_method(fn, a, b, e, small_num):
    while math.fabs(a - b) > e:
        y = (a + b - small_num) / 2
        z = (a + b + small_num) / 2
        if fn(y) < fn(z):
            b = z
        else:
            a = y 
    return (a + b) / 2, fn((a + b) / 2)

if __name__ == '__main__':
    def f(x):
        return(127 / 4 * x**2 - 61 / 4 * x + 2)
    e = 0.00001
    a = -5
    b = 5
    print(half_division_method(f, a, b, e, e / 2))