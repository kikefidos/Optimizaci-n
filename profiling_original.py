# profiling_original.py
import cProfile
import codigo_original

if __name__ == "__main__":
    cProfile.run('codigo_original.encontrar_primos(10000)')