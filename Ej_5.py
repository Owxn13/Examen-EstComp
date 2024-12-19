import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def jackknife_transacciones():
    df = pd.read_csv(r'D:\Trabajos y Prácticas\V Semestre\Estadística Computacional\Datos.csv')
    datos = df['TransactionAmount']
    n = len(datos)
    medias_jackknife = []
    
    for i in range(n):
        muestra = np.delete(datos, i)
        medias_jackknife.append(np.mean(muestra))
    
    media_jackknife = np.mean(medias_jackknife)
    varianza_jackknife = np.var(medias_jackknife) * (n - 1)
    
    plt.figure(figsize=(10, 6))
    plt.hist(medias_jackknife, bins=50, density=True, alpha=0.7)
    plt.axvline(x=media_jackknife, color='r', linestyle='--', label='Media Jackknife')
    plt.title('Distribución de las medias Jackknife del monto de transacciones')
    plt.xlabel('Media')
    plt.ylabel('Densidad')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("Resultados del análisis Jackknife:")
    print(f"1. Media Jackknife del monto de transacciones: {media_jackknife:.2f}")
    print(f"2. Varianza Jackknife de las medias estimadas: {varianza_jackknife:.2f}")

jackknife_transacciones()