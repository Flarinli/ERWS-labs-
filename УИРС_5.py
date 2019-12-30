import random
import math

def RadDegrees(*angles):
    return [angle * 180 / math.pi for angle in angles]
def DegreesRad(*angles):
    return [angle * math.pi / 180 for angle in angles]
#Создание матрицы
def Create_Matrix(m,n):
    return [[random.uniform(0, 100) for _ in range(n)] for _ in range(m)]
#Вывод матрицы на экран
def Print_Matrix(matrix):
    for i in matrix:
        for j in i:
            print(f"{j:.4f}",end = ' ')
        print()
#Сложение матриц
def Sum_Of_Matrix(a,b):
    res = max(a,b)[:]
    if b > a:
        a,b = b,a
    for i in range(len(b)):
        for j in range(min(len(a[0]),len(b[0]))):
            res[i][j] += b[i][j]
    return res
#Умножение матриц
def Matrix_Multiply(matrix1,matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("умножение невозможно")
        return [[],[],[]]
    res = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res
#Трансформация системы координат.
def TransformCS(matrix, alfa = 0, beta = 0, gamma = 0, dx = 0, dy = 0, dz = 0, key = "degrees", T = False):
    if key == "degrees":
        alfa,beta,gamma = DegreesRad(alfa, beta, gamma)
    Rx = [[  1,                0,                0  ],
          [  0,   math.cos(alfa),   math.sin(alfa)  ],
          [  0,  -math.sin(alfa),   math.cos(alfa)  ]]

    Ry = [[  math.cos(beta),   0,  -math.sin(beta)  ],
          [  0,                1,                0  ],
          [  math.sin(beta),   0,   math.cos(beta)  ]]

    Rz = [[  math.cos(gamma),  math.sin(gamma),  0  ],
          [ -math.sin(gamma),  math.cos(gamma),  0  ],
          [  0,                0,                1  ]]

    dR = [[ dx ],
          [ dy ],
          [ dz ]]

    return Sum_Of_Matrix(Matrix_Multiply(Transposition(Matrix_Multiply(Matrix_Multiply(Rx, Ry), Rz)), matrix), dR) if T else Sum_Of_Matrix(Matrix_Multiply(Matrix_Multiply(Matrix_Multiply(Rx, Ry), Rz), matrix), dR)

#main
def Transposition(X):
    if not(len(X) and len(X[0])):
        print('Матрицу нельзя транспонировать')
        return
    res = X[:]
    for  i in range(len(res)):
        for j in range(len(res[0])):
            if i > j:
                res[i][j], res[j][i] = res[j][i], res[i][j]
    return res
#Переход из связной в нормальную
def Svaz_Norm(X):
    psi   = float(input("Введите угол рыскания: "))
    pitch = float(input("Введите угол тангажа: "))
    gamma = float(input("Введите угол крена"))
    return TransformCS(X, gamma, psi, pitch)
def Norm_Svaz(X):
    psi   = float(input("Введите угол рыскания: "))
    pitch = float(input("Введите угол тангажа: "))
    gamma = float(input("Введите угол крена"))
    return TransformCS(X, gamma, psi, pitch,T = True)
def Norm_Scor(X):
    psi   = float(input("Введите угол пути: "))
    theta = float(input("Введите угол наклона к горизонту касательной к траектории ЛА: "))
    gamma = float(input("Введите угол крена в скоростной СК: "))
    return TransformCS(X, gamma, psi, theta)
def Scor_Norm(X):
    psi   = float(input("Введите угол пути: "))
    theta = float(input("Введите угол наклона к горизонту касательной к траектории ЛА: "))
    gamma = float(input("Введите угол крена в скоростной СК: "))
    return TransformCS(X, gamma, psi, theta, T = True)
def Norm_Traect(X):
    psi   = float(input("Введите угол пути: "))
    theta = float(input("Введите угол наклона к горизонту касательной к траектории ЛА: "))
    gamma = 0
    return TransformCS(X, gamma, psi, theha)
def Traect_Norm(X):
    psi   = float(input("Введите угол пути: "))
    theta = float(input("Введите угол наклона к горизонту касательной к траектории ЛА: "))
    gamma = 0
    return TransformCS(X, gamma, psi, theha, T = True)
def Traect_Scor(X):
    gamma = float(input("Введите угол крена в скоростной СК: "))
    return TransformCS(X, alfa = gamma)
def Scor_Traect(X):
    gamma = float(input("Введите угол крена в скоростной СК: "))
    return TransformCS(X, alfa = gamma, T = True)
def Scor_Svaz(X):
    alfa = float(input("Введите угол атаки (угол между ОХ связанной СК и проекцией скорости на ХОУ): "))
    beta = float(input("Введите угол скольжения между вектором скорости и его проекцией на вертикальную плоскость симметрии ЛА: "))
    return TransformCS(X, beta = beta, gamma = alfa)
def Svaz_Scor(X):
    alfa = float(input("Введите угол атаки (угол между ОХ связанной СК и проекцией скорости на ХОУ): "))
    beta = float(input("Введите угол скольжения между вектором скорости и его проекцией на вертикальную плоскость симметрии ЛА: "))
    return TransformCS(X, beta = beta, gamma = alfa, T = True)

#Пример
matrix = Create_Matrix(3,1)
Print_Matrix(matrix)
print()
matrix = Svaz_Scor(matrix)
Print_Matrix(matrix)
print()
matrix = Scor_Svaz(matrix)
Print_Matrix(matrix)
