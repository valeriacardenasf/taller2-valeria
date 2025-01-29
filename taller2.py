import numpy as np

mu = 3
sigma = 0.5 
n=100
vals = np.random.normal(loc=mu, scale=sigma, size=n)
print(vals)