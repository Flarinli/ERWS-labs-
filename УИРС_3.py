import math
def Sum(x,y):
    res = []
    if len(x) != len(y):
        print("Размеры векторов не совпадают")
        return
    for i in range(len(x)):
        res += [x[i] + y[i]]
    return res

def ScMult(x,y):
    res = float()
    if len(x) != len(y):
        print("Размеры векторов не совпадают")
        return
    for i in range(len(x)):
        res += x[i] * y[i]
    return res

def VecMult3(x,y):
    return [(x[1]*y[2] - y[1]*x[2]), (x[0]*y[2]-y[0]*x[2]), (x[0]*y[1] - y[0]*x[1])]

def ModuleOfVec(x):
    res = float()
    for i in x:
        res+=i**2
    return res**(1/2)

def Angle(x,y):
    return math.acos(ScMult(x,y) / (ModuleOfVec(x) * ModuleOfVec(y)))

def ModuleOfVecMult(x,y):
    return ModuleOfVec(x)*ModuleOfVec(y)*math.sin(Angle(x,y))

def MatrFromVec(arr):
    res = []
    for v in arr:
        res.append(v)
    return res
def PrintMatr(A):
    for line in A:
        print(line)
def SwapRows(A,row1,row2):
    A[row1],A[row2] = A[row2],A[row1]

def DivideRow(A,row,divider):
    A[row] = [a / divider for a in A[row]]

def CombineRows(A,row1,row2,weight):
    A[row1] = [(a1 + weight * a2) for a1,a2 in zip(A[row1],A[row2])]

def GaussDet(A):
    res = 1
    Column = 0 #Column отвеяает по сути за столбец и за диагональный элемент матрицы
    while(Column < (len(A[0])-1)):
        CurRow = None
        for r in range(Column, len(A)):
            if ((CurRow is None) or (abs(A[r][Column]) > abs(A[CurRow][Column]))):
                CurRow = r
        if CurRow != Column:
            SwapRows(A,CurRow,Column)
            res *= -1
        if A[Column][Column] == 0:
            Column += 1
            continue

        res*=A[Column][Column]
        DivideRow(A,Column, A[Column][Column])

        for r in range(Column+1,len(A)):
            CombineRows(A,r,Column, -A[r][Column])
        Column += 1
    for i in range(len(A)):
        res *= A[i][i]
    return res

def Minor(Matrix,i):
    res = []
    for m in range(len(Matrix[0])-1):
        temp = []
        for n in range(len(Matrix[0])):
            if (n == i):
                continue
            temp.append(Matrix[m][n])
        res.append(temp)
    return res

def VecMult(vectors):
    if len(vectors[0]) != (len(vectors) + 1):
        return "Векторное произведение невозможно"
    res = []
    Matrix = MatrFromVec(vectors)
    for i in range(len(Matrix[0])):
        TempMatr = Minor(Matrix,i)
        res.append((-1)**(i) * GaussDet(TempMatr))
    return res

print("Операции с векторами\n")
N = int(input("Введите размерность векторов: "))
k = int(input("Введите количество векторов: "))
arr = [] #Список векторов
for i in range(k):
    print(f"Введите координаты вектора {i+1}:")
    arr.append([float(input(f"{j}-я координата: ")) for j in range(N)])
print(f"Сумма первых двух данных векторов: {Sum(arr[0],arr[1])}")
print(f"Скалярное произведение первых двух данных векторов: {ScMult(arr[0],arr[1])}")
print(f"Векторное произведение первых двух данных векторов: {VecMult([arr[0],arr[1]])}")
input()
