import os
def mostrarMenu():
    print('1 - xxxxxxxxxxx')
    print('2 - yyyyyyyyyyy')
    print('3 - zzzzzzzzzzz')
    print('4 - Salir')

mostrarMenu()
opcion = input('ingresar opcion: ')
while opcion >= '1' and opcion <= '4':
    opcion = input('ingresar opcion:')

while opcion != '4':
    if opcion == '1':
        print('xxxxxxxxxxx')
    elif opcion == '2':
        print('yyyyyyyyyyy')
    elif opcion == '3':
        print('zzzzzzzzzzz') 
    input()
    os.system('cls')
    mostrarMenu()
    opcion = input('ingresar opcion: ')