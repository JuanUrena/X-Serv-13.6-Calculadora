#!/usr/bin/python3
import sys
# tomar datos desde la ejecucion del programa
from sys import argv
# importa una funcion concreta para no tener que llamarla de sys
# Obtengo los datos desde la linea de comandos
operacion = (argv[1])
num1 = float((argv[2]))
num2 = float((argv[3]))
# Compruebo el valor de la operacion para llevarla acabo
try:
    if operacion == 'suma':
        Resultado = num1+num2
    elif operacion == 'resta':
        Resultado = num1-num2
    elif operacion == 'multiplicacion':
        Resultado = num1*num2
    elif operacion == 'division':
        Resultado = num1/num2
    else:
        print('caso especial consultar a Pacheco')
    print(Resultado)
except ZeroDivisionError:
    print("no se puede dividir por cero")
