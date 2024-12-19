import numpy as np
import matplotlib.pyplot as plt

def simular_dados():
    n_simulaciones = 100000
    exitos = 0
    distribucion_seis = []
    
    for i in range(n_simulaciones):
        seis = 0
        for j in range(10):
            if np.random.randint(1, 7) == 6:
                seis += 1
        distribucion_seis.append(seis)
        if seis >= 4:
            exitos += 1
    
    probabilidad = exitos / n_simulaciones
    
    plt.figure(figsize=(10, 6))
    plt.hist(distribucion_seis, bins=range(12), density=True, alpha=0.7)
    plt.title('Distribución del número de seis obtenidos en 10 lanzamientos')
    plt.xlabel('Número de seis')
    plt.ylabel('Frecuencia relativa')
    plt.grid(True)
    plt.show()
    
    print(f"Total experimentos: {n_simulaciones:,}")
    print(f"Experimentos exitosos: {exitos:,}")
    print(f"Probabilidad: {probabilidad:.4f}")

simular_dados()