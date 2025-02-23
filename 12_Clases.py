#Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

#Clases#

#Definición

#Clase con constructor, funciones y propiedades privadas y públicas

print("--------------------------------------------------------------------------")
print("-                              Clases                                    -")
print("--------------------------------------------------------------------------")
print("-    Definición de Clase | Variables Publicas y Funciones                -")
print("--------------------------------------------------------------------------")
print("- class Person:                                                          -")
print("-     def __init__(self, name, surname, alias='Por Defecto'):            -")
print("-         self.full_name = f'{name} {surname}' #Variable Publica         -")
print("-     def walk(self): #Funciones en las Clases                           -")
print("-         print(f'{self.full_name} está caminando')                      -")
print("--------------------------------------------------------------------------")

class Person:                         #Alias lo ponemos por defecto en caso de que no se le pase nada
    def __init__(self, name, surname, alias="Por defecto"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        #self.__name = name  # Propiedad privada

    #def get_name(self):
        #return self.__name

    #Funcion en una Clase
    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Gorka", "Sanchez")
print(my_person.full_name)
my_person.walk()

my_person = Person("Gorka", "Sanchez", "Gorkii14")
print(my_person.full_name)
my_person.walk()

my_person.full_name = "Héctor de León (El loco de los perros)"
print(my_person.full_name)

my_person.full_name = 14
print(my_person.full_name)


print("--------------------------------------------------------------")
print("-                 Clases con Varible Privada                 -")
print("--------------------------------------------------------------")
print("- class Person2:                                             -")
print("-      def __init__(self, name):                             -")
print("-         self._name = name        #Varible Privada          -")
print("--------------------------------------------------------------")

class Person2:
    def __init__(self, name):
        self.__name = name
        

    def get_name(self):
        return self.__name

my_other_person = Person2("Brais")
print(my_other_person.get_name())

#A pesar de cambiar el nombre no me va a dejar modificarlo porque es privada
my_other_person.__name = "Gorka"
print(my_other_person.get_name())


