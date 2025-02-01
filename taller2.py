import numpy as np
import pandas as pd

mu = 5
sigma = 1 
n=100
vals = np.random.normal(loc=mu, scale=sigma, size=n)
print(vals)

df = pd.DataFrame(vals)

#Estadisticas Descriptivas
print(df.describe())

print(df.head())

#Generar números aleatorios con una distribución exponencial

mu = 3
vals_nuevos = np.random.exponential(scale=mu, size=n)

df = pd.DataFrame(vals_nuevos)