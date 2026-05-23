# Mi primer programa en Python
# Este es un comentario - Python lo ignora
# Las líneas que empiezan con '#' son para que los humanos lean notas.

# ============================================
# 1. CREACIÓN DE VARIABLES
# ============================================
# Una variable es como una "caja" donde guardamos información.
# En Python, no necesitas decir qué tipo de dato es, él lo adivina.

nombre = "Estudiante"   # Esto es un texto (se llama 'string')
edad = 25               # Esto es un número entero (se llama 'integer')
altura = 1.75           # Esto es un número con decimales (se llama 'float')

# ============================================
# 2. OPERACIONES BÁSICAS
# ============================================
# Podemos hacer matemáticas simples con los números.

anio_actual = 2024
# Calculamos en qué año cumplirás 100 años:
# (100 - edad) nos da los años que faltan, y lo sumamos al año actual.
anio_cumple_100 = anio_actual + (100 - edad)

# ============================================
# 3. IMPRIMIR RESULTADOS (OUTPUT)
# ============================================
# La función print() muestra información en la pantalla.

# Imprimir un texto simple
print("¡Hola, Mundo!")
print("Bienvenido a Python")

# Imprimir el valor de una variable
print("Tu nombre es:")
print(nombre)

# F-STRINGS (Cadenas formateadas) - ¡Muy importante!
# Esto permite mezclar texto y variables fácilmente.
# Usamos la letra 'f' antes de las comillas y ponemos la variable entre llaves {}
mensaje_bienvenida = f"Hola {nombre}, tienes {edad} años y mides {altura} metros."
print(mensaje_bienvenida)

# Imprimir el resultado de nuestro cálculo
print(f"Cumplirás 100 años aproximadamente en el año {anio_cumple_100}")
