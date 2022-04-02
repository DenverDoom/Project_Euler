import numpy as np

arr = np.arange(1,21)
lcm = np.lcm.reduce(arr)

print(lcm)