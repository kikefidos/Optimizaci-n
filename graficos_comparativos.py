# graficos_comparativos.py
import matplotlib.pyplot as plt

def crear_grafico_comparativo():
    versiones = ['Original', 'Optimizada', 'NumPy']
    tiempos = [45.32, 2.15, 1.98]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(versiones, tiempos, color=['red', 'blue', 'green'])
    plt.title('Comparación de Tiempos de Ejecución')
    plt.ylabel('Tiempo (segundos)')
    
    # Añadir valores en las barras
    for bar, tiempo in zip(bars, tiempos):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{tiempo}s', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('comparacion_tiempos.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    crear_grafico_comparativo()