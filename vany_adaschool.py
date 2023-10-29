# Define variables de diferentes tipos de datos primitivos
entero = 42
flotante = 3.14
cadena = "Hola, soy una cadena"
booleano = True

# Concatena las variables en una cadena, convirtiendo las no cadenas según sea necesario
resultado_cadena = cadena + " - " + str(entero) + " - " + str(flotante) + " - " + str(booleano)

# Imprime el resultado de la concatenación
print("Concatenación:", resultado_cadena)

# Límites de enteros y flotantes en Python (añade comentarios)
# Enteros: Python 3 no tiene límite práctico, puede crecer tanto como la memoria lo permita.
# Flotantes: Límite de precisión debido a la representación en coma flotante de la CPU.

# Fórmula para la suma de los primeros n números pares
# La suma de los primeros n números pares es n * (n + 1)
n = 5
suma_pares = n * (n + 1)

# Imprime el resultado de la suma de los primeros n números pares
print("Suma de los primeros", n, "números pares:", suma_pares)

