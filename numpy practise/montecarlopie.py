import numpy as np

n = 1000000
x = np.random.rand(n)
y = np.random.rand(n)

inside = (x**2 + y**2) <= 1
pi_estimate = 4 + np.sum(inside)/n
print(pi_estimate)