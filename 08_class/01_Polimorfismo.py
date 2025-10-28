from os import system

if system("clear") != 0: system("cls")

#! 🧩 Repaso rápido: una clase básica
class auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Informacion del auto, Marca: {self.marca}, modelo: {self.modelo}")

mi_auto = auto("Toyota", "Corola")
mi_auto.mostrar_info()



class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        print(f"El {self.marca} esta encendido!")

#! La clase Auto hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo) #? Llamamos al constructor del padre
        self.puertas = puertas

    def mostrar_info(self):
        print(f"El auto {self.modelo},{self.marca} tiene {self.puertas} puertas")

mi_vehiculo = Auto("Toyota", "Corola", 4)
mi_vehiculo.encender()
mi_vehiculo.mostrar_info()