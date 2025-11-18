# codigo_original.py
import time

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def encontrar_primos(limite):
    primos = []
    for i in range(1, limite + 1):
        if es_primo(i):
            primos.append(i)
    return primos

if __name__ == "__main__":
    inicio = time.time()
    primos = encontrar_primos(100000)
    fin = time.time()

    print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")
    print(f"Se encontraron {len(primos)} números primos")