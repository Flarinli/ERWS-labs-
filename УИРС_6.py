import math
#Интегратор

#Шаг интегрирования системы ДУ 1-ого порядка методом Эйлера
#Вид списков:
#   In[0]   - длина шага интегрирования (равна отношению времени интегрирования к количеству его шагов)
#   In[1:]  - данные необходимые для вычислений(первые n значений соответсвуют исходным значениям функций правых частей( n = len(RValues)), Далее идут списки значений, необходимых для вычисления каждой правой части)
#   RValues - список функций правых частей
def Step_of_Euler_method(In = [], RValues = []):
    if (In or RValues) == False:
        return
    X = In[1:]
    for count, RValue in enumerate(RValues):
        X[count][0] += RValue(X[count]) * In[0]
    return X

#Интегрирование системы ДУ 1-ого порядка методом Эйлера
#Вид списков:
#   In[0]   - длина отрезка интегрирования
#   In[1]   - количество шагов интегрирования
#   In[2:]  - данные необходимые для вычислений(первые n значений соответсвуют исходным значениям функций правых частей( n = len(RValues)), Далее идут списки значений, необходимых для вычисления каждой правой части)
#   RValues - список функций правых частей
def Euler_method(In = [], RValues = []):
    print("Метод Эйлера")
    if (In or RValues) == False:
        return []
    X = In[2:]
    out = []
    for i in range(In[1]):
        for count, value in enumerate(Step_of_Euler_method([In[0] / In[1]] + X, RValues)):
            X[count][0] = value[0]
    out = [value[0] for value in X]
    return out

#Пример использования:
print("Интегрирование системы ДУ 1-ого порядка методом Эйлера:\n")

#Переход из радиан в градусы и из градусов в радианы:
def RadDegrees(angle):
    return angle * 180 / math.pi
def DegreesRad(angle):
    return angle * math.pi / 180

#Функции правых частей
print("rX(In) = In[1] * math.cos(In[2])")
print("rY(In) = In[1] * math.sin(In[2])")
def rX(In):
    return In[1]*math.cos(In[2])
def rY(In):
    return In[1]*math.sin(In[2])

print("Введите промежуток времени:")
t = float(input("t: "))
print("Введите количество итераций:")
k = int(input("k: "))
print("Введите начальные координаты цели:")
x = float(input("x: "))
y = float(input("y: "))
print("Введите скорость цели:")
v = float(input("v: "))
print("Введите угол курса цели: ")
course = DegreesRad(float(input("course:")))
In = [t, k, [x, v, course], [y, v, course] ]
RValues = [rX, rY]
print(Euler_method(In, RValues))
input()
