from keras.utils import np_utils
from keras.models import load_model
import numpy as np

import matplotlib.pyplot as plt
# from numpy.lib.function_base import append
import os
import random


file_name_list = [["./testexe/OSU!.exe", 1],
                  ]


dataf = np.array([])
dataf = np.resize(dataf, (0, 100, 100, 1))
targetf = np.array([])
targetf = np.resize(targetf, (0, 1))

for file_name in file_name_list:
    file_stats = os.stat(file_name[0])
    ln = file_stats.st_size
    rem = ln % 10000
    a = np.fromfile(file_name[0], dtype='uint8', count=ln-rem)
    g = a.reshape(-1, 1)
    g = g / 255
    g = g.reshape(-1, 100, 100, 1)
    data = np.array([i for i in g])
    target = np.array([[file_name[1]] for i in g])
    dataf = np.concatenate((dataf, data), axis=0)
    targetf = np.concatenate((targetf, target), axis=0)


# index = [i for i in range(len(dataf))]
# random.shuffle(index)
# dataf = dataf[index]
# targetf = targetf[index]
# test_y = np_utils.to_categorical(targetf, 2)

print(len(dataf))

dataf = dataf.reshape(-1, 100, 1)
plt.imshow(dataf, cmap=plt.cm.gray, aspect="auto")
plt.colorbar()
plt.show()
# model = load_model('minosmodel.h5')


# scores = model.evaluate(dataf, test_y, verbose=1)
# print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
