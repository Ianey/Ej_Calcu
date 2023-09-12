#              PROYECTO FINAL 
#              PYTHON BÁSICO
# Nombre: Jesica Ianey Aguilar Soto
# Fecha de entrega: 04/08/2023

'''
Realizar una calculadora básica que tenga un menú con las operaciones básicas. 
En el caso de la división tendrá que considerarse que uno no puede dividir entre 0. 
Hacer el conteo de cada operación que se haga, además imprimir el resultado de todas las operaciones 
como en un historial el número de operaciones (usar diccionario de preferencia). 

'''
def suma (numero_1, numero_2):
    return numero_1 + numero_2

def resta (numero_1, numero_2):
    return numero_1 - numero_2

def multiplicacion (numero_1, numero_2):
    return numero_1 * numero_2

def division (numero_1, numero_2):
    if numero_2 !=0:
        return numero_1 / numero_2

conteo_operaciones ={'Suma': 0, 'Resta': 0, 'Multiplicación': 0, 'División': 0}

while True: 

    print('1) Suma')
    print('2) Resta')
    print('3) Multiplicación')
    print('4) División')
    print('5) Salir\n')

    operacion = int(input('Selecciona la operación que deseas realizar: '))
    

    if operacion == 1:
        print('Elegiste realizar una suma\n')
        numero_1 = float(input('Ingresa el primer número: '))
        numero_2 = float(input('Ingresa el segundo número: '))
        resultado = suma(numero_1, numero_2)
        print(f'La suma es: {numero_1} + {numero_2}  = {resultado}\n')
        conteo_operaciones['Suma'] += 1

    elif operacion == 2:
        print('Elegiste realizar una resta\n')
        numero_1 = float(input('Ingresa el primer número: '))
        numero_2 = float(input('Ingresa el segundo número: '))
        resultado = resta(numero_1, numero_2)
        print(f'La resta es: {numero_1} - {numero_2}  = {resultado}\n')
        conteo_operaciones['Resta'] += 1

    elif operacion == 3:
        print('Elegiste realizar una multiplicación\n')
        numero_1 = float(input('Ingresa el primer número: '))
        numero_2 = float(input('Ingresa el segundo número: '))
        resultado = multiplicacion(numero_1, numero_2)
        print(f'El producto es: {numero_1} * {numero_2}  = {resultado}\n')
        conteo_operaciones['Multiplicación'] += 1

    elif operacion == 4: 
        print('Elegiste realizar una división\n')
        numero_1 = float(input('Ingresa el primer número: '))
        numero_2 = float(input('Ingresa el segundo número: '))
        if numero_2 != 0:
            resultado = division(numero_1, numero_2)
            print(f'La división es: {numero_1} / {numero_2}  = {resultado}\n')
            conteo_operaciones['División'] += 1
        else:
            print('ERROR: no es posible dividir entre 0\n')  

    elif operacion == 5:
        print('¡Hasta pronto! c: \n')
        break

    else: 
        print('Ingresa una opción válida\n')

    
    resultados = {'Resultado de la Suma': suma (numero_1, numero_2), 
                  'Resultado de la Resta': resta (numero_1, numero_2), 
                  'Resultado de la Multiplicacion': multiplicacion (numero_1, numero_2), 
                  'Resultado de la Division': division (numero_1, numero_2) }
    
print('Historial de conteo de operaciones: \n')
for operacion, conteo in conteo_operaciones.items():
    print(f'{operacion}: {conteo} operaciones')

print ('Historial de resultado de operaciones: \n')
for resultado in resultados.values():
    print(resultado)


