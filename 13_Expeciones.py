#Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=32030

##Exception Handling

numberOne = 5
numberTwo = 1
numberTwo = "1"

#Excepción base: try except

print("--------------------------------------------------")
print("-        Excepciones | Control de Errores        -")
print("--------------------------------------------------")
print("--------------------------------------------------")
print("-     Variables :      -")
print("------------------------")
print("-   numberOne =  5     -")
print("-   numberTwo =  1     -")
print("-   numberTwo = '1'    -")
print("------------------------")
print("-------------------------------------------")
print("-try:                                     -")
print("-    print(numberOne + numberTwo)         -")
print("-    print('No se ha producido un error') -")
print("-except:                                  -")
print("-    print('Se ha producido un error')    -")
print("-------------------------------------------")
print("--------------------------------------------------------")
print("-   Forzamos el Error y el programa va por el Except   -")
print("--------------------------------------------------------")

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

#Flujo completo de una excepción: try except else finally

print("-------------------------------------------------------------------------")
print("-    Flujo completo de una excepcion : try | except | else | finally    -")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print("-try:                                                                   -")
print("-    print(numberOne + numberTwo)                                       -")  
print("-    print('No se ha producido un error')                               -")
print("-except:                                                                -")
print("-    print('Se ha producido un error')                                  -")
print("-else:                                                                  -")
print("-    print('La ejecución continúa correctamente')                       -")
print("-finally:                                                               -")
print("-    print('La ejecución continúa')                                     -")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

#Excepciones por tipo

print("--------------------------------------------------")
print("-            Excepciones por tipo                -")
print("--------------------------------------------------")
print("--------------------------------------------------")
print("-try:                                            -")
print("-    print(numberOne + numberTwo)                -")
print("-    print('No se ha producido un error')        -")
print("-except ValueError:                              -")
print("-    print('Se ha producido un ValueError')      -")
print("-except TypeError:                               -")
print("-    print('Se ha producido un TypeError')       -")
print("--------------------------------------------------")

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

#Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
  print(my_random_error_name)

class prueba:
  pass