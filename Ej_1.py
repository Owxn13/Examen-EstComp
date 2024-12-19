import numpy as np
import matplotlib.pyplot as plt

def simular_cartas():
    n_simulaciones = 100000
    exitos = 0
    ases = [0, 13, 26, 39]
    resultados = []
    
    for i in range(n_simulaciones):
        mano = np.random.choice(52, 5, replace=False)
        for as_carta in ases:
            if as_carta in mano:
                exitos += 1
                resultados.append(1)
                break
        else:
            resultados.append(0)
    
    probabilidad = exitos / n_simulaciones
    
    plt.figure(figsize=(10, 6))
    plt.plot(np.cumsum(resultados) / np.arange(1, n_simulaciones + 1))
    plt.axhline(y=probabilidad, color='r', linestyle='--', label='Probabilidad final')
    plt.title('Convergencia de la probabilidad de obtener al menos un as')
    plt.xlabel('Número de simulaciones')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"Total simulaciones: {n_simulaciones:,}")
    print(f"Manos con al menos un as: {exitos:,}")
    print(f"Probabilidad: {probabilidad:.4f}")

simular_cartas()