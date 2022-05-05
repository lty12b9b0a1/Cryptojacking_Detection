import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# ser.open()
n_sample = 16000


print('Start')
winds = []
targets = []

t = np.array([i/8920 for i in range(n_sample)])


filename = 'D:/Desktop/final_data/1080ti/overall/timespy.csv'
count = 0
with open(filename, 'r', encoding='utf-8') as file_to_read:
    while True:
        lines = file_to_read.readline()  # 整行读取数据
        count = count + 1
        if not lines:
            break
        if count >= 5:
            volte, = [float(i) for i in lines.split(',')]
            targets.append((volte-2.5)*4)
        if count >= 16004:
            break

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8, 2.8)
ax = fig.add_subplot(111)
ax.set_xticks([], [])
ax.set_yticks([], [])
ax.set(ylim=[0, 6])
ax.plot(t, targets)

# dataf = np.array([i for i in targets])
# dataf1 = np.delete(dataf, [i for i in range(16000) if dataf[i] < 1.4])
# t1 = np.delete(t, [i for i in range(16000) if dataf[i] < 1.4])
# print(len(t1), len(dataf1))
# ax1 = fig.add_subplot(212)
# ax1.set_xticks([], [])
# ax1.set_yticks([], [])
# ax1.set(ylim=[0, 6])
# ax1.plot(t1, dataf1)
plt.show()
