from os import system

if system("clear") != 0: system("cls") 

class cuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo #* protegido (no se debe tocar desde fuera)

    def depositar(self, monto):
        self._saldo += monto
        print(f"Nuvo saldo: {self._saldo}")

    def __mostrar_saldo(self): #* Privado
        print(f"EL saldo de la cuenta es: {self._saldo}")    


cuenta = cuentaBancaria("juan", 1000)

cuenta.depositar(500)
cuenta.depositar(1000)

#! cuenta.__mostrar_saldo() ❌ → Error, es "privado"

#? 🧩 4️⃣ Métodos estáticos y de clase

class calculadora:
    @staticmethod

    def sumar(a, b):
        return a + b

print(f"La suma de 5 y 7 es: {calculadora.sumar(5, 7)}")

#? ➡️ Es ideal cuando el método no depende de atributos de la clase.

class Persona:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

    @classmethod
    def total_personas(cls):
        print(f"Se han creado {cls.contador} personas.")


p1 = Persona("Ana")
p2 = Persona("Juan")

Persona.total_personas()


#? 🎭 5️⃣ Polimorfismo y sobreescritura

class Animal:
    def sonido(self):
        print("Sonido generico")

class Perro:
    def sonido(self):
        print("Guau!")

class Gato:
    def sonido(self):
        print("Miau!")


animales = [Perro(), Gato(), Animal()]

for animal in animales:
    animal.sonido()


#? 🧮 6️⃣ Ejercicio práctico (mini proyecto)
#? Crea una estructura con herencia y polimorfismo:
#? Clase padre Dispositivo
#? Clases hijas: Celular, Laptop
#? Cada una tiene un método mostrar_info() con un comportamiento distinto
#? Un método estático que calcule el número total de dispositivos creados

class Dispositivo:
    # Atributo de clase compartido por todas las instancias
    total_dispositivos = 0

    def __init__(self, marca, modelo):
        # Atributos protegidos (por convención)
        self._marca = marca
        self._modelo = modelo
        Dispositivo.total_dispositivos += 1

    def mostrar_info(self):
        print(f"Dispositivo genérico: {self._marca} {self._modelo}")

    @staticmethod
    def saludar():
        print("Bienvenido al sistema de dispositivos 💻📱")

    @classmethod
    def cantidad_total(cls):
        print(f"Total de dispositivos creados: {cls.total_dispositivos}")


# ---------------------------- #
# Clases hijas
# ---------------------------- #
class Celular(Dispositivo):
    def __init__(self, marca, modelo, camara):
        super().__init__(marca, modelo)
        self._camara = camara

    def mostrar_info(self):  # Polimorfismo (sobreescribe el método)
        print(f"📱 Celular {self._marca} {self._modelo} con cámara de {self._camara}MP")


class Laptop(Dispositivo):
    def __init__(self, marca, modelo, ram):
        super().__init__(marca, modelo)
        self._ram = ram

    def mostrar_info(self):  # Polimorfismo
        print(f"💻 Laptop {self._marca} {self._modelo} con {self._ram}GB de RAM")


# ---------------------------- #
# Uso del programa
# ---------------------------- #

# Llamamos al método estático
Dispositivo.saludar()

# Creamos objetos
celular1 = Celular("Samsung", "S23", 108)
celular2 = Celular("Apple", "iPhone 15", 48)
laptop1 = Laptop("Asus", "Vivobook", 16)

# Los mostramos (cada uno se comporta distinto)
celular1.mostrar_info()
celular2.mostrar_info()
laptop1.mostrar_info()

# Llamamos al método de clase
Dispositivo.cantidad_total()
