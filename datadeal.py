from keras.backend import concatenate
from keras.preprocessing.sequence import TimeseriesGenerator
import numpy as np
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data = np.array([[i] for i in range(2000)])
data2 = np.array([[i] for i in range(1000)])
targets = np.array([[1] for i in range(20000)])
# print(data)
x_train_scaled = scaler.fit_transform(data.astype(np.float32))
x_train_scaled2 = scaler.fit_transform(data2.astype(np.float32))
dataa = concatenate((x_train_scaled, x_train_scaled2), axis=0)
print(dataa)
# data_gen = TimeseriesGenerator(data, targets,
#                                length=100, sampling_rate=1, stride=100, shuffle=True,
#                                batch_size=100)
# batch_0 = data_gen[0]
# x, y = batch_0
# print(data_gen[0])
