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

