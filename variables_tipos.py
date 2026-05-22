# VARIABLES Y TIPOS DE DATOS EN PYTHON
# Las variables son espacios donde guardamos información

# ===== STRINGS (texto) =====
nombre = "Juan"
ciudad = "Madrid"
print(f"Mi nombre es {nombre} y vivo en {ciudad}")

# ===== INTEGERS (números enteros) =====
edad = 25
año_nacimiento = 1998
numero_hermanos = 3
print(f"Tengo {edad} años")

# ===== FLOATS (números decimales) =====
altura = 1.75
peso = 72.5
promedio = 8.5
print(f"Mi altura es {altura} metros")

# ===== BOOLEANS (Verdadero/Falso) =====
es_estudiante = True
tiene_trabajo = False
print(f"¿Soy estudiante? {es_estudiante}")

# ===== VERIFICAR TIPO DE DATO =====
print(f"\nTipo de 'nombre': {type(nombre)}")
print(f"Tipo de 'edad': {type(edad)}")
print(f"Tipo de 'altura': {type(altura)}")
print(f"Tipo de 'es_estudiante': {type(es_estudiante)}")

# ===== CONVERSIÓN DE TIPOS =====
numero_texto = "42"
numero_entero = int(numero_texto)  # Convertir texto a entero
print(f"\n'{numero_texto}' convertido a entero: {numero_entero}")

numero = 100
numero_como_texto = str(numero)  # Convertir entero a texto
print(f"{numero} convertido a texto: '{numero_como_texto}'")
