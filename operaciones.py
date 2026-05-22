# OPERACIONES MATEMÁTICAS EN PYTHON

# ===== SUMA =====
a = 10
b = 5
suma = a + b
print(f"Suma: {a} + {b} = {suma}")

# ===== RESTA =====
resta = a - b
print(f"Resta: {a} - {b} = {resta}")

# ===== MULTIPLICACIÓN =====
multiplicacion = a * b
print(f"Multiplicación: {a} × {b} = {multiplicacion}")

# ===== DIVISIÓN =====
division = a / b
print(f"División: {a} ÷ {b} = {division}")

# ===== DIVISIÓN ENTERA (sin decimales) =====
division_entera = a // b
print(f"División entera: {a} // {b} = {division_entera}")

# ===== MÓDULO (resto de la división) =====
modulo = a % b
print(f"Módulo: {a} % {b} = {modulo}")

# ===== POTENCIA =====
potencia = 2 ** 3  # 2 elevado a 3
print(f"Potencia: 2 ** 3 = {potencia}")

# ===== OPERACIONES CON TEXTO =====
print("\n--- OPERACIONES CON TEXTO ---")
texto1 = "Hola"
texto2 = "Mundo"
concatenacion = texto1 + " " + texto2
print(f"Concatenación: '{concatenacion}'")

# Repetir texto
repeticion = "Python " * 3
print(f"Repetición: '{repeticion}'")

# ===== OPERACIONES CON LISTAS =====
print("\n--- OPERACIONES CON LISTAS ---")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_combinada = lista1 + lista2
print(f"Listas combinadas: {lista_combinada}")

lista_repetida = [0] * 5
print(f"Lista repetida: {lista_repetida}")

# ===== INCREMENTO Y DECREMENTO =====
print("\n--- INCREMENTO Y DECREMENTO ---")
contador = 10
print(f"Valor inicial: {contador}")
contador = contador + 1  # Incrementar en 1
print(f"Después de +1: {contador}")
contador += 5  # Incrementar en 5 (forma abreviada)
print(f"Después de +=5: {contador}")
contador -= 3  # Decrementar en 3
print(f"Después de -=3: {contador}")
