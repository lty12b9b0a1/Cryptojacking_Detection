import numpy as np
import os

file_name = "ethminer.exe"
file_stats = os.stat(file_name)
ln = file_stats.st_size
rem = ln % 10000
a = np.fromfile(file_name, dtype='uint8', count=ln-rem)

g = a.reshape(-1, 1)

g = g / 255
g = g.reshape(-1, 100, 1)

k = np.array([i for i in g])
data = np.concatenate((k, g), axis=0)
target1 = np.array([[0] for i in g])
print(len(target1), len(k))
# a = np.fromfile('',)
