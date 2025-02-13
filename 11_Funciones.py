#Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=26619

###Functiones###

#Definición
# Definición
#Prueba

def my_function():
    print("Esto es una función")

my_function()

#Función con parámetros de entrada/argumentos

def sum_two_values (first_value , second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)

#Lo interpreta como cadena de caracteres y los concatena
sum_two_values("5","7")

#Le paso un entero , pero lo convierto en entero "int"
sum_two_values(int("5"),int("7"))


sum_two_values(1.4, 5.2)



#Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

#None
my_result = sum_two_values(1.4, 5.2)
print(my_result)

"""
my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Moure", name="Brais")

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

def prueba ():
    
    my_condition = 0

    while my_condition < 10:
            print(my_condition)
            my_condition += 2
    else:  # Es opcional
            print("Mi condición es mayor o igual que 10")

    print("La ejecución continúa")


prueba()
"""