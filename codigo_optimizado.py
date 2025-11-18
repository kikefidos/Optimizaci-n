# codigo_optimizado.py
import time
import numpy as np
import math

def es_primo_optimizado(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True

def encontrar_primos_optimizado(limite):
    return [i for i in range(2, limite + 1) if es_primo_optimizado(i)]

def encontrar_primos_numpy(limite):
    numeros = np.arange(2, limite + 1)
    mascara = np.array([es_primo_optimizado(n) for n in numeros])
    return numeros[mascara]

# Medición de tiempo para versión con list comprehensions
inicio1 = time.time()
primos_opt = encontrar_primos_optimizado(100000)
fin1 = time.time()

# Medición de tiempo para versión con NumPy
inicio2 = time.time()
primos_numpy = encontrar_primos_numpy(100000)
fin2 = time.time()

print(f"Tiempo versión optimizada: {fin1 - inicio1:.2f} segundos")
print(f"Tiempo versión NumPy: {fin2 - inicio2:.2f} segundos")
print(f"Se encontraron {len(primos_opt)} números primos")