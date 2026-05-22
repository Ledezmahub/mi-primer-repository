# ESTRUCTURAS DE CONTROL EN PYTHON
# IF/ELSE, FOR, WHILE, LISTAS, DICCIONARIOS

# ===== IF / ELSE / ELIF =====
print("--- IF / ELSE / ELIF ---")
edad = 18

if edad >= 18:
    print(f"Tienes {edad} años - Eres mayor de edad")
elif edad >= 13:
    print(f"Tienes {edad} años - Eres adolescente")
else:
    print(f"Tienes {edad} años - Eres menor")

# ===== OPERADORES LÓGICOS =====
print("\n--- OPERADORES LÓGICOS ---")
tiene_carnet = True
tiene_auto = False

if tiene_carnet and tiene_auto:
    print("Puedes conducir tu auto")
elif tiene_carnet or tiene_auto:
    print("Tienes al menos carnet o auto")
else:
    print("No tienes carnet ni auto")

# ===== FOR - Recorrer una lista =====
print("\n--- FOR - RECORRER LISTAS ---")
frutas = ["manzana", "plátano", "naranja", "fresa"]

print("Frutas disponibles:")
for fruta in frutas:
    print(f"  - {fruta}")

# ===== FOR - Recorrer con range =====
print("\nNúmeros del 1 al 5:")
for numero in range(1, 6):  # range(inicio, fin) - fin NO se incluye
    print(f"  Número: {numero}")

# ===== FOR - Recorrer con índice =====
print("\nFrutas con índice:")
for indice in range(len(frutas)):
    print(f"  Índice {indice}: {frutas[indice]}")

# ===== WHILE - Repetir mientras sea verdadero =====
print("\n--- WHILE ---")
contador = 1
print("Contando del 1 al 3:")
while contador <= 3:
    print(f"  Contador: {contador}")
    contador += 1

# ===== BREAK - Salir del bucle =====
print("\n--- BREAK ---")
print("Buscando el número 3:")
for num in range(1, 10):
    if num == 3:
        print(f"  ¡Encontré el {num}! Saliendo...")
        break
    print(f"  Revisando: {num}")

# ===== CONTINUE - Saltar iteración =====
print("\n--- CONTINUE ---")
print("Números pares del 1 al 10:")
for num in range(1, 11):
    if num % 2 == 1:  # Si es impar, saltar
        continue
    print(f"  {num}")

# ===== LISTAS =====
print("\n--- LISTAS ---")
numeros = [10, 20, 30, 40, 50]
print(f"Lista: {numeros}")
print(f"Primer elemento: {numeros[0]}")
print(f"Último elemento: {numeros[-1]}")
print(f"Largo de la lista: {len(numeros)}")

# Agregar elementos
numeros.append(60)
print(f"Después de agregar 60: {numeros}")

# Eliminar elementos
numeros.remove(20)
print(f"Después de eliminar 20: {numeros}")

# ===== DICCIONARIOS =====
print("\n--- DICCIONARIOS ---")
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid",
    "profesión": "Ingeniero"
}

print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")

# Recorrer diccionario
print("Información completa:")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# ===== COMPRENSIÓN DE LISTAS =====
print("\n--- COMPRENSIÓN DE LISTAS ---")
# Crear lista de números al cuadrado
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados de 1 a 5: {cuadrados}")

# Crear lista de números pares
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares del 1 al 10: {pares}")
