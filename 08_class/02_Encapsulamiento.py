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