# profiling_optimizado.py
import cProfile
import codigo_optimizado

if __name__ == "__main__":
    cProfile.run('codigo_optimizado.encontrar_primos_optimizado(10000)')