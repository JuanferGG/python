# 🐍 Curso Personal de Python — by Juan Fernando Calderón Vargas

Este repositorio contiene todos mis estudios, prácticas y experimentos realizados durante mi proceso de aprendizaje con **Python**.  
He abarcado desde los fundamentos hasta conceptos avanzados como **expresiones regulares, POO y web scraping**.

---

## 📘 Contenido del aprendizaje

### 1️⃣ Fundamentos de Python
- Variables, tipos de datos y operadores
- Estructuras de control (`if`, `else`, `for`, `while`)
- Funciones (`def`, parámetros, valores por defecto, return)
- Módulos y paquetes (`import`, `from ... import ...`)
- Entrada y salida de datos (`input()`, `print()`)

---

### 2️⃣ Expresiones Regulares (Regex)
- Introducción al módulo `re`
- Uso de patrones básicos (`\w`, `\d`, `\s`, `.`)
- Anclas (`^`, `$`, `\b`)
- Cuantificadores:
  - `*` → 0 o más repeticiones  
  - `+` → 1 o más repeticiones  
  - `?` → 0 o 1  
  - `{n}`, `{n,m}` → repeticiones específicas
- Grupos y rangos: `()`, `[a-z]`, `[A-Z0-9]`
- Ejercicios prácticos: búsqueda de palabras, validación de textos y filtrado de archivos

---

### 3️⃣ Web Scraping
- Peticiones HTTP con `requests`
- Limpieza de HTML usando **BeautifulSoup**
- Extracción de:
  - Título de la página
  - Precios, textos y etiquetas específicas (`find`, `find_all`)
- Uso de **headers personalizados** y simulación de navegador
- Expresiones regulares combinadas con HTML para buscar patrones
- Análisis básico de SEO:
  - Verificación de títulos `<title>`
  - Detección de encabezados `h1`
  - Ejemplo con `argparse` para pasar URLs desde la terminal

---

### 4️⃣ Programación Orientada a Objetos (POO)
- Definición de clases y objetos
- Constructor `__init__`
- Atributos de clase y de instancia
- Métodos de instancia
- Encapsulamiento con atributos protegidos (`_atributo`)
- **Herencia** y reutilización de código
- **Polimorfismo** (sobrescritura de métodos)
- **Métodos estáticos** (`@staticmethod`)
- **Métodos de clase** (`@classmethod`)
- Ejemplo práctico:
  - Clase base `Dispositivo`
  - Clases hijas `Celular` y `Laptop`
  - Contador global de instancias
  - Diferentes comportamientos por clase

---

### 5️⃣ Automatización y Testing
- Uso de **Playwright** para pruebas automáticas de UI
- Ejecución de pruebas con `pytest`
- Selectores por rol y validación de contenido (`get_by_role`, `expect`)
- Ejemplo práctico: pruebas sobre la web oficial de Playwright

---

## 🚀 Próximos pasos
Estos son los temas que continuaré explorando próximamente:

- **Archivos y persistencia de datos:** lectura/escritura con `open()`, `csv`, `json`
- **Bases de datos locales:** SQLite con `sqlite3`
- **Manejo de errores:** `try`, `except`, `finally`, `raise`
- **Decoradores y funciones lambda**
- **POO avanzada:** propiedades, métodos mágicos, clases abstractas
- **Automatización web avanzada con Playwright y Selenium**
- **FastAPI o Flask:** para crear APIs en Python

---

## ⚙️ Dependencias instaladas
```bash
pip install requests
pip install beautifulsoup4
pip install playwright
pip install pytest
