import serial
import numpy as np
import matplotlib.pyplot as plt
import time
import csv
from tqdm import tqdm
ser = serial.Serial('COM3', 115200, timeout=1)
# ser.open()
n_sample = 1600000


print('Start')
winds = []
targets = []

for i in tqdm(range(n_sample + 400)):
    if i == 400:
        start = time.time()
    wind = ser.read(1)
    winds.append(wind)

end = time.time()
print('End of reading...')
print('Sampling rate is ', n_sample / (end-start))
t = np.array([i/(n_sample / (end-start)) for i in range(n_sample)])


f = open("serial_output.csv", "w", encoding="utf-8", newline="")
csv_writer = csv.writer(f)
csv_writer.writerow([n_sample / (end-start)])
for i in range(n_sample + 400):
    if i >= 400:
        try:
            voltt = winds[i].decode()
            temp = ord(voltt)
            target = (temp + 256) * 2 * (5.0 / 1023.0)
            csv_writer.writerow([target])
            targets.append(target)
        except Exception as e:
            csv_writer.writerow([2.6])
            targets.append(2.6)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(ylim=[2.4, 3.8], title='--', ylabel='Y-Axis', xlabel='X-Axis')
ax.plot(t, targets)
plt.show()
