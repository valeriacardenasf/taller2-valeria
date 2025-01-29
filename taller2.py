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