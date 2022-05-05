import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fs = 8920  # sampling rate

data_path = 'serial_output.csv'
window_sz = 102400


# read data
df = pd.read_csv(data_path, header=None)
data = df.to_numpy()
data = data[1:].squeeze()
sample = data[fs:fs+window_sz]

# plot fft
freq = np.fft.fftfreq(window_sz, d=1/fs)
fft = np.abs(np.fft.fft(sample))
fft[freq < 10] = 0

plt.plot(np.fft.fftshift(freq), np.fft.fftshift(fft))
plt.show()
