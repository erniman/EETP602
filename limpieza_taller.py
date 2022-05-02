#!/usr/bin/env python
import random
import time
import sys
import subprocess as sp
sp.call('clear',shell=True)    #limpio pantalla

#creo lista
foo = ['Coria', 'Formento', 'Gimenez', 'Gutierrez', 'Leyes',
'Moyano', 'Ojeda', 'Olmedo', 'Piccirilli', 'Ramirez', 'Sanchez', 'Suarez', 'Troncoso', 'Villa', 'Salvetti']

# Imprimo banner
print "SISTEMA DE SELECCION PARA LIMPIEZA DEL TALLER ELECTRONICA\n"
print "Este sistema selecciona dos estudiantes de forma aleatoria para que realicen tareas de limpieza en el taller."
print " \n"
print ("Lista de estudiantes que pueden salir sorteados:\n")

# Muestro estudiantes en pantalla
for items in foo:
    print (items)
    time.sleep(0.5)

#Pregunto si hay alumnos ausentes y los quito de la lista
#http://www.leccionespracticas.com/python/recorrer-una-lista-y-eliminar-elementos-en-python-resuelto

#Pausa para continuar
print "\n"
raw_input("Listo? Presionar ENTER para continuar...\n")

# Guardo en variables
opcion1 = random.choice(foo)
opcion2 = random.choice(foo)

# Pregunto si hay duplicados
if opcion1 == opcion2:
    opcion2 = random.choice(foo)

# Muestro progress bar
print "\n Procesando datos..."
for i in range(100+1):
    time.sleep(0.04)
    sys.stdout.write(('='*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
    sys.stdout.flush()

# Muestro resultados
print "\n"
print "      ***** Estudiante Titular seleccionado ------> ", opcion1
print "      ***** Estudiante Titular seleccionado ------> ", opcion2
print "\n"

#Pregunto si algun alumno esta ausente
