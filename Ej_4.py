import pandas as pd
import numpy as np

def bootstrap_varianza_transaccion():
    df = pd.read_csv(r'D:\Trabajos y Prácticas\V Semestre\Estadística Computacional\Datos.csv')
    datos = df['TransactionDuration']
    
    n_bootstrap = 10000
    varianzas_bootstrap = np.zeros(n_bootstrap)
    
    for i in range(n_bootstrap):
        muestra = np.random.choice(datos, size=len(datos), replace=True)
        varianzas_bootstrap[i] = np.var(muestra)
    
    varianza_estimada = np.mean(varianzas_bootstrap)
    
    ic_inferior, ic_superior = np.percentile(varianzas_bootstrap, [2.5, 97.5])
    
    return varianza_estimada, (ic_inferior, ic_superior)

varianza, intervalo_confianza = bootstrap_varianza_transaccion()

print("Resultados del análisis bootstrap:")
print(f"1. Varianza estimada del tiempo de transacción: {varianza:.2f}")
print(f"2. Intervalo de confianza del 95%:")
print(f"- Límite inferior: {intervalo_confianza[0]:.2f}")
print(f"- Límite superior: {intervalo_confianza[1]:.2f}")