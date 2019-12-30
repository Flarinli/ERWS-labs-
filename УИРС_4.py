import random, copy
CONST_MIN = 0
CONST_MAX = 100

#Создание матрицы
def Create_Matrix(m,n):
    return [[random.uniform(CONST_MIN, CONST_MAX) for _ in range(n)] for _ in range(m)]
#Вывод матрицы на экран
def Print_Matrix(matrix):
    for i in matrix:
        for j in i:
            print(f"{j:.4f}",end = ' ')
        print()
#Сложение матриц
#Структура, передаваемая в функцию должна выглядеть следующим образом:
#[row(1)[], row(2)[],..., row(n)[]]
def Sum_Of_Matrix(a,b):
    res = copy.deepcopy(max(a,b))
    if b > a:
        a,b = b,a
    for i in range(len(b)):
        for j in range(min(len(a[0]),len(b[0]))):
            res[i][j] += b[i][j]
    return res
#Умножение матриц
#Структура, передаваемая в функцию должна выглядеть следующим образом:
#[row(1)[], row(2)[],..., row(n)[]]. Параметр b может также являться числом
def Matrix_Multiply(a,b):
    if len(a[0]) != len(b):
        print("умножение невозможно")
        return []
    res = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]
    return res
#Умножение матрицы на число
#Структура, передаваемая в функцию должна выглядеть следующим образом:
#[row(1)[], row(2)[],..., row(n)[]]
def Multiply_Matrix_And_Number(matrix,weight):
    return [[el * weight for el in row] for row in matrix]
#Обмен двух строк матрицы
def Swap_Rows(A,row1,row2):
    A[row1],A[row2] = A[row2],A[row1]
#Деление строки на число
def Divide_Row(A,row,divider):
    A[row] = [a / divider for a in A[row]]
#Сложение одной строки матрицы со второй, умноженной на число
def Combine_Rows(A,row1,row2,weight):
    A[row1] = [(a1 + weight * a2) for a1,a2 in zip(A[row1],A[row2])]
#Определитель матрицы методом Гаусса
def Gauss_Det(A):
    res = 1
    Column = 0 #Column отвечает по сути за столбец и за диагональный элемент матрицы
    while(Column < (len(A[0])-1)):
        CurRow = None
        for r in range(Column, len(A)):
            if ((CurRow is None) or (abs(A[r][Column]) > abs(A[CurRow][Column]))):
                CurRow = r
        if CurRow != Column:
            Swap_Rows(A,CurRow,Column)
            res *= -1
        if A[Column][Column] == 0:
            Column += 1
            continue

        res*=A[Column][Column]
        Divide_Row(A,Column, A[Column][Column])

        for r in range(Column+1,len(A)):
            Combine_Rows(A,r,Column, -A[r][Column])
        Column += 1
    for i in range(len(A)):
        res *= A[i][i]
    return res
#Дополнительный минор
#Структура, передаваемая в функцию должна выглядеть следующим образом:
#[row(1)[], row(2)[],..., row(n)[]]
def Additional_Minor(matrix,i,j):
    res = []
    for m in range(len(matrix)):
        temp = []
        for n in range(len(matrix[0])):
            if (m == i) or (n == j):
                continue
            temp.append(matrix[m][n])
        if temp == []:
            continue
        res.append(temp)
    return Gauss_Det(res)
#Алгебраическое дополнение
#Структура, передаваемая в функцию должна выглядеть следующим образом:
#[row(1)[], row(2)[],..., row(n)[]]
def Cofactor(matrix,i,j):
    return Additional_Minor(matrix,i,j) * (-1)**(i+j)
#Транспонирование матрицы
#Структура, передаваемая в функцию должна выглядеть следующим образом:
#[row(1)[], row(2)[],..., row(n)[]]
def T(A):
    matrix = copy.deepcopy(A)
    if not(len(matrix) and len(matrix[0])):
        print('Матрицу нельзя транспонировать')
        return matrix
    for  i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i > j:
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    return matrix
#Обратная матрица
#Структура, передаваемая в функцию должна выглядеть следующим образом:
#[row(1)[], row(2)[],..., row(n)[]]
def Inverse_Matrix(matrix):
    if Gauss_Det(matrix) == 0:
        print("Для данной матрицы не существует обратная матрица ")
        return matrix
    Matrix_Of_Cofactors = [[Cofactor(matrix,i,j) for j in range(len(matrix[0]))] for i in range(len(matrix))]
    return Multiply_Matrix_And_Number(T(Matrix_Of_Cofactors),1 / Gauss_Det(matrix))

print("Введите размерность матрицы 1: ")
n = int(input("n: "))
matrix1 = Create_Matrix(n,n)
print("1-я матрица: ")
Print_Matrix(matrix1)
print()

print("Введите размерность матрицы 2: ")
n = int(input("n: "))
matrix2 = Create_Matrix(n,n)
print("2-я матрица: ")
Print_Matrix(matrix2)
print()

print("Сумма матриц 1 и 2: ")
Print_Matrix(Sum_Of_Matrix(matrix1,matrix2))
print()

print("Умножение 1-й матрицы на 2-ю")
Print_Matrix(Matrix_Multiply(matrix1,matrix2))
print()

print("Нахождение обратной матрицы для матрицы 1: ")
print("Исходная матрица: ")
Print_Matrix(matrix1)
print()
print("обратная матрица: ")
Print_Matrix(Inverse_Matrix(matrix1))
print()
print("Умножение исходной матрицы на обратную (проверка): ")
Print_Matrix(Matrix_Multiply(matrix1,Inverse_Matrix(matrix1)))
input()
