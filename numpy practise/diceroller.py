import numpy as np

rools = np.random.randint(1,7,size=(100,2))
sum = rools.sum(axis=1)

freq = np.bincount(sum)[2:]

for i ,f in enumerate(freq, start = 2):
    print(f"sum {i}: {f}times")