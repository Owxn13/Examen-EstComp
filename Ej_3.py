import pandas as pd
import numpy as np

def bootstrap_saldo_cuentas():
    df = pd.read_csv(r'D:\Trabajos y Prácticas\V Semestre\Estadística Computacional\Datos.csv')
    datos = df['AccountBalance']
    
    n_bootstrap = 10000
    medias_bootstrap = np.zeros(n_bootstrap)
    
    for i in range(n_bootstrap):
        muestra = np.random.choice(datos, size=len(datos), replace=True)
        medias_bootstrap[i] = np.mean(muestra)
    
    media_estimada = np.mean(medias_bootstrap)
    
    ic_inferior, ic_superior = np.percentile(medias_bootstrap, [5, 95])
    
    return media_estimada, (ic_inferior, ic_superior)

media, intervalo_confianza = bootstrap_saldo_cuentas()

print("Resultados del análisis bootstrap:")
print(f"1. Media estimada del saldo: {media:.2f}")
print(f"2. Intervalo de confianza del 90%:")
print(f"- Límite inferior: {intervalo_confianza[0]:.2f}")
print(f"- Límite superior: {intervalo_confianza[1]:.2f}")