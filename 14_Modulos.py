#Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=34583

#Modulos

#from math import pi as PI_VALUE
#import math


#print (math.pi)
#print (math.pow(2, 8))
#print(PI_VALUE)

print("--------------------------------------------------------------------")
print("-                            Módulos                               -")
print("--------------------------------------------------------------------")
print("-   Con esto podemos coger porciones de codigo de otros archivos   -")
print("-   Y reutilizarlo en otros programas.                             -")
print("-   P.EMPL : con my_module                                         -")
print("                                                                    ")
print("-   Primero lo importamos :                                        -")
print("--------------------------------------------------------------------")
print("-   import my_module                                               -")
print("--------------------------------------------------------------------")

import my_module

print("--------------------------------------------------------------------------------")
print("-   Luego podemos llamar a las diferentes partes del codigo que hay dentro :   -")
print("--------------------------------------------------------------------------------")
print("-   my_module.sumValue(5, 3, 1)            -")
print("-   my_module.printValue('Hola Python!')   -")
print("--------------------------------------------")

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")

print("---------------------------------------------------------------------------")
print("-   Otra forma de hacerlo es importar solo unicamente parte del modulo    -")
print("---------------------------------------------------------------------------")
print("-   importamos de la siguiente forma :                                    -")
print("---------------------------------------------------------------------------")
print("-   'from my_module import sumValue'                                      -")
print("---------------------------------------------------------------------------")
print("-   sumValue(5, 3, 1)                                                     -")
print("---------------------------------------------------------------------------")   

from my_module import sumValue
#from my_module import sumValue, printValue

sumValue(5, 3, 1)
#printValue("Hola python")