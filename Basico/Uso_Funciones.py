#Funciones Sin Retorno
#Al llamar a la función #Suma, y pasandole los parametros nos imprimira directamente el resultado de la suma.

#En este caso unicamente con llamarla ya nos devolvera el resultado de la suma.
def suma (numero1,numero2):
    print(numero1+numero2)

suma(5,7)#12


#Funciones Con Retorno
#1.- creamos la Función con los parametros a utilizar
#Y dentro lo que vayamos a hacer con esos parametros , guardado en una variable
#Y lo retornamos.
def suma_con_retorno(numero1,numero2):
    suma=numero1+numero2
    return suma


#2.- Guardamos el resultado de la función en una variable
prueba = suma_con_retorno(2,1)
suma_final = suma(5,7)
suma_fnal2 =suma_con_retorno(2,1)

print(suma_fnal2)#3
print(suma_final)#None  
print(prueba)#3