
#? 1. Introducción a las Clases en Python
#? Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
#? Nos permite agrupar datos (atributos o propiedades) y funciones (métodos) en un solo lugar.

from os import system
if system("clear") != 0: system("cls")

OPENAI_KEY = ""
DEEPSEEK_API_KEY = ""

#! Ejemplo básico de una clase
class Coche:
    #? atributo de clase (comparte todas las instancias)
    tipo = "Vehiculo de cuatro ruedas"
    ruedas = 4

    #? método especial que es el que construye el objeto
    #? se llama automáticamente este método cuando creas la instancia
    #TODO para valores por defecto usar propiedad="valor", y todos deben tener si hay valor por defecto y los q no None.
    def __init__(self, marca, modelo, color):
        #? atributos de la instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} arrancó!")

mi_coche = Coche("Toyota", "Corola", "rojo")
mi_coche.arrancar()

print(f"\nMarca del coche: {mi_coche.marca}")
print(f"Tipo de coche: {mi_coche.tipo}")

#? Encapsulación: es ocultar los detalles internos de una clase y exponer solo la interfaz pública
#? Crear una clase para llamar a la AI de OpenAI, DeepSeek O LO QUE SEA

import requests

class AI_API:
  def __init__(self, api_key, url, model):
    self.api_key = api_key
    self.url = url
    self.model = model

  def call(self, prompt):
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {self.api_key}"
    }
    data = {
      "model": self.model,
      "messages": [{"role": "user", "content": prompt}]
    }

    try:
      response = requests.post(self.url, json=data, headers=headers)
      res_json = response.json()
      print(res_json["choices"][0]["message"]["content"])
    except requests.exceptions.RequestException as e:
      print(f"Error en la solicitud: {e}")
      return None

print("\nOPEN_AI:")
openai_api = AI_API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")

openai_api.call("Escribe un breve poema sobre la programación")

print("\nDEEPSEEK:")
deepseek_api = AI_API(DEEPSEEK_API_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")

deepseek_api.call("Escribe un breve poema sobre la programación")