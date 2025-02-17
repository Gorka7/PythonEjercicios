#Ejercicio
#Escribir una función que reciba una muestra de números en una lista 
#y devuelva su media.


numero = input("Introduce un número: ")
numero=int(numero)
mi_lista_numeros = []


for numeros in numero:
    media = sum(mi_lista_numeros) / len(mi_lista_numeros)
    print("La media de los números es: ", media)


