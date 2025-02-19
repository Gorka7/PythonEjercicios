
#Funciones Sin Retorno
#Al llamar a la función #Suma, y pasandole los parametros nos imprimira directamente el resultado de la suma.

#En este caso unicamente con llamarla ya nos devolvera el resultado de la suma.

def suma (numero1,numero2):
    print(numero1+numero2)

suma(5,7)


#Funciones Con Retorno
#Al llamar a la función #Suma_con_retorno, y pasandole los parametros nos devolvera el resultado de la suma.
def suma_con_retorno(numero1,numero2):
    suma=numero1+numero2
    return suma

print(".")
prueba = suma_con_retorno(2,1)
suma_final = suma(5,7)
suma_fnal2 =suma_con_retorno(2,1)

print(suma_fnal2)
print(suma_final)
print(prueba)