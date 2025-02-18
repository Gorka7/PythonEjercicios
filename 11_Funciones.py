#Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=26619

###Functiones###

#Definición

print("-------------------------------------------")
print("-            Funciones                    -")
print("-------------------------------------------")
print("-      Declaración de Función             -")
print("-------------------------------------------")
print("-  def my_function():                     -")
print("-      print('Esto es una función')       -")
print("-  my_function()                          -")
print("-------------------------------------------")


def my_function():  
        print('Esto es una función') 
    
my_function()  

my_function()


print("-------------------------------------------------------")
print("-  sum_two_values (first_value , second_value):       -")
print("-      print(first_value + second_value)              -")
print("-  my_function()                                      -")
print("-------------------------------------------------------")
#Función con parámetros de entrada/argumentos

print("----------------------------------------------------------------") 
print("-       def sum_two_values (first_value , second_value):       -")
print("-           print(first_value + second_value)                  -")
print("-                                                              -")
print("----------------------------------------------------------------")

def sum_two_values (first_value , second_value):
    print(first_value + second_value)

print("-------------------------------------------------------")
print("-  sum_two_values (first_value , second_value):       -")
print("-      print(first_value + second_value)              -")
print("-  my_function()                                      -")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("- sum_two_values(5, 7)                                -")
print("-------------------------------------------------------")
sum_two_values(5, 7) 

print("----------------------------------------------------------------")
print("-       sum_two_values(5, 7)  |                                -")
print("----------------------------------------------------------------")
sum_two_values(5, 7)

print("----------------------------------------------------------------")
print("-       sum_two_values(54754, 71231)                           -")
print("----------------------------------------------------------------")
sum_two_values(54754, 71231)

print("---------------------------------------------------------------------------------------------------")
print("-       sum_two_values('5','7') | #Lo interpreta como cadena de caracteres y los concatena        -")
print("---------------------------------------------------------------------------------------------------")
#Lo interpreta como cadena de caracteres y los concatena
sum_two_values("5","7")

print("------------------------------------------------------------------------------------------------------------")
print("-       sum_two_values(int('5'),int('7'))  | #Le paso un entero , pero lo convierto en entero 'int'        -")
print("------------------------------------------------------------------------------------------------------------")
#Le paso un entero , pero lo convierto en entero "int"
sum_two_values(int("5"),int("7"))

print("----------------------------------------------------------------")
print("-       sum_two_values(1.4, 5.2)                               -")
print("----------------------------------------------------------------")
sum_two_values(1.4, 5.2)



print("--------------------------------------------------------------------------")
print("-        def sum_two_values_with_return(first_value, second_value):      -")
print("-            my_sum = first_value + second_value                         -")
print("-            return my_sum                                               -")
print("--------------------------------------------------------------------------")

##Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum #Esto devuelve 6.6

#Esto devuelve None
my_result = sum_two_values(1.4, 5.2)

print("--------------------------------------------------------------------------------------------------------------------------")   
print("-     my_result = sum_two_values(1.4, 5.2) | Nos Devuelve 'None' porque la Funcion 'sum_two_values' No tiene retorno     -")
print("-     print(my_result)                                                                                                   -")
print("--------------------------------------------------------------------------------------------------------------------------")

print(my_result)

print("----------------------------------------------------------------")
print("- my_result = sum_two_values_with_return(10, 5)                -")
print("- print(my_result)                                             -")
print("----------------------------------------------------------------") 

my_result = sum_two_values_with_return(10, 5)
print(my_result)


#Función con parámetros de entrada/argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}")

print("----------------------------------------------------------------")
print("- def print_name(name, surname):                               -")
print("-     print(f'{name} {surname}')                               -")
print("-                                                              -")
print("- print_name('Moure','Brais')                                  -")
print("----------------------------------------------------------------")

print_name("Moure","Brais")

print("----------------------------------------------------------------")
print("-         Si lo queremos ordenado , Hay que indicarselo        -")
print("----------------------------------------------------------------")
print("-         print_name(surname='Moure',name='Brais')             -")
print("----------------------------------------------------------------")
print_name(surname='Moure',name='Brais')
print("----------------------------------------------------------------")   


#Función con parámetros de entrada/argumentos por defecto

print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("-       Función con parámetros de entrada/argumentos por defecto                                                                                -")
print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("-     def print_name_with_default(name, surname,alias='Sin alias'):                                                                             -")
print("-         print(f'{name} {surname} {alias}')                                                                                                    -")
print("-   En el momento en el que NO metamos un 3 parametro | print_name_with_default('Brais', 'Moure') | Establece por defecto | alias 'Sin alias'   -")
print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#Establecemos en alias "Sin alias" , ya que a la funcion le estamos pasando 3 valores
#
def print_name_with_default(name, surname,alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

#Función con parámetros de entrada/argumentos arbitrarios

print("----------------------------------------------------------------")  
print("-   Función con parámetros de entrada/argumentos arbitrarios   -")
print("----------------------------------------------------------------")
print("-   def print_upper_texts(*texts):                             -")
print("-       print(type(texts))                                     -")
print("-       for text in texts:                                     -")
print("-           print(text.upper())                                -")
print("-                                                              -")
print("----------------------------------------------------------------")

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")


