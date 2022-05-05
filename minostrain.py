from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, GlobalAveragePooling2D
from keras.losses import categorical_crossentropy
from keras.optimizers import adam_v2
import numpy as np
# from numpy.lib.function_base import append
import os
import random


file_name_list = [["./testexe/eth.exe", 1],
                  ["./testexe/eth2.exe", 1],
                  ["./testexe/dag.exe", 1],
                  ["./testexe/reg.exe", 1],
                  ["./testexe/WeChat.exe", 0],
                  ["./testexe/ugc_assistant.exe", 0],
                  ["./testexe/cloudmusic.exe", 0],
                  ]


dataf = np.array([])
dataf = np.resize(dataf, (0, 100, 100, 1))
targetf = np.array([])
targetf = np.resize(targetf, (0, 1))

# preprocess
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

# shuffle
index = [i for i in range(len(dataf))]
random.shuffle(index)
dataf = dataf[index]
targetf = targetf[index]
train_y = np_utils.to_categorical(targetf, 2)


print(len(dataf))


model = Sequential()
model.add(Conv2D(16, (3, 3), activation='relu', input_shape=(100, 100, 1)))
model.add(Conv2D(16, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(GlobalAveragePooling2D())
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

model.compile(loss=categorical_crossentropy, optimizer=adam_v2.Adam(), metrics=['accuracy'])

batch_size = 30
epochs = 50
model.fit(dataf, train_y, batch_size=batch_size, epochs=epochs)
model.save('minosmodel.h5')
