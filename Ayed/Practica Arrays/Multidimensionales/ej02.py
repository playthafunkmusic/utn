def carga(x):
    for i in range(f):
        for j in range(c):
            x[i][j] = int(input(f'fila {i} columna {j}: '))

def suma(x):
    for i in range(f):
        d1 = x[i][i]
        d2 = x[i][c-1-i]
        print (d1+d2)

f = c = 2
a = [[0]*c for k in range(f)]
carga(a)
print(a)
suma(a)
