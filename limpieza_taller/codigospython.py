    #!/usr/bin/env python
import random
import time
import sys
import subprocess as sp

ausentes = 'si'

def clear():
    sp.call('clear',shell=True)

def imprimo_lista(lista):
    for items in lista:
        print (items)
        time.sleep(0.1)

def barra_progreso():
    for i in range(100+1):
        time.sleep(0.03)
        sys.stdout.write(('='*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
        sys.stdout.flush()

def borro_ausentes(lista, alumno):
    while alumno != "no":
        alumno = raw_input("Ingresar Apellido (escribir -no- para salir): ")
        for x in lista:
            if x == alumno:
                foo.remove(x)

clear()
lista = (["2112","1212","121","2143123"])
foo = (lista)

print "SISTEMA DE SELECCION PARA LIMPIEZA DEL TALLER ELECTRONICA\n"
print "Este sistema selecciona dos estudiantes de forma aleatoria para que realicen tareas de limpieza en el taller."
print " \n"
print ("Lista de estudiantes que pueden salir sorteados:\n")

# Muestro estudiantes en pantalla
imprimo_lista(foo)

#Pregunto si hay alumnos ausentes y los quito de la lista
print "\nHay estudiantes ausentes?"
borro_ausentes(foo, ausentes)

#Imprimo lista definitiva
clear()
#sp.call('clear',shell=True)    #limpio pantalla
print ("\nLista de estudiantes PRESENTES que pueden salir sorteados:\n")
imprimo_lista(foo)

#Pausa para continuar
raw_input("\nListo? Presionar ENTER para continuar...\n")

# Guardo en variables
opcion1 = random.choice(foo)
opcion2 = random.choice(foo)

# Pregunto si hay duplicados
if opcion1 == opcion2:
    opcion2 = random.choice(foo)

# Muestro progress bar
print "Procesando datos..."
barra_progreso()

print "\n      ***** Estudiante Titular seleccionado ------> ", opcion1
print "      ***** Estudiante Titular seleccionado ------> ", opcion2
print "\n"
