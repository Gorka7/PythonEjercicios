class Persona:
    def __init__(self,nombre,apellido,alias="Sin Alias"):
        self.nombre_completo = f"{nombre} {apellido} {alias}"

    def andando(self):
        print(f"{self.nombre_completo} esta caminando")

mi_persona = Persona("Gorka","Sanchez")
print(mi_persona.nombre_completo) 
mi_persona.andando()

otra_persona = Persona('Gorka','Sanchez','Gorkii14')
print(otra_persona.nombre_completo)
otra_persona.andando()
