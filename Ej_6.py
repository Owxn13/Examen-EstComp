import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def jackknife_mediana_sesgo():
    df = pd.read_csv(r'D:\Trabajos y Prácticas\V Semestre\Estadística Computacional\Datos.csv')
    datos = df['CustomerAge']
    n = len(datos)
    mediana_original = np.median(datos)
    medianas_jackknife = []
    
    for i in range(n):
        muestra = np.delete(datos, i)
        medianas_jackknife.append(np.median(muestra))
    
    media_medianas_jackknife = np.mean(medianas_jackknife)
    sesgo = (n - 1) * (media_medianas_jackknife - mediana_original)
    
    plt.figure(figsize=(10, 6))
    plt.hist(medianas_jackknife, bins=50, density=True, alpha=0.7)
    plt.axvline(x=mediana_original, color='r', linestyle='--', label='Mediana original')
    plt.axvline(x=media_medianas_jackknife, color='g', linestyle='--', label='Media de medianas')
    plt.title('Distribución de las medianas Jackknife de las edades')
    plt.xlabel('Mediana')
    plt.ylabel('Densidad')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("Resultados del análisis Jackknife:")
    print(f"1. Mediana original de las edades: {mediana_original:.2f}")
    print(f"2. Media de las medianas Jackknife: {media_medianas_jackknife:.2f}")
    print(f"3. Sesgo Jackknife estimado: {sesgo:.2f}")

jackknife_mediana_sesgo()