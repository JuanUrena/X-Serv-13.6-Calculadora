#!/usr/bin/python3
import sys
# tomar datos desde la ejecucion del programa
from sys import argv
# importa una funcion concreta para no tener que llamarla de sys
# Obtengo los datos desde la linea de comandos
try:
    operacion = (argv[1])
    num1 = float((argv[2]))
    num2 = float((argv[3]))
# Compruebo el valor de la operacion para llevarla acabo

    if operacion == 'suma':
        Resultado = num1+num2
        print(Resultado)
    elif operacion == 'resta':
        Resultado = num1-num2
        print(Resultado)
    elif operacion == 'multiplicacion':
        Resultado = num1*num2
        print(Resultado)
    elif operacion == 'division':
        Resultado = num1/num2
        print(Resultado)
    else:
        print('Operacón no detectada')
        print('Pruebe con "suma", "resta", "multiplicacion" o "division"')
    
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
except IndexError:
    print('Error: La entrada debe ser:' 
    print('python3 calculadora.py <operación> <num1> <num2>') 
except ValueError:
    print('Error: La entrada debe ser:') 
    print('python3 calculadora.py <operación> <num1> <num2>') 
    
