import matplotlib.pyplot as plt
import numpy as np
filename = './data/1.20/4096-128cudacore.csv'

filename2 = './data/access_stride=1.csv'
pos = []
time1 = []
time2 = []
targert = []
targert2 = []
voltes = []
voltes2 = []
tempmax = 0
count = 0
with open(filename, 'r', encoding='utf-8') as file_to_read:
    while True:
        count = count + 1
        lines = file_to_read.readline()  # 整行读取数据
        if not lines:
            break
        if count >= 5:
            if count % 1 == 0:
                p_tmp, volte = [float(i) for i in lines.split(',')]
                time1.append(p_tmp)
                voltes.append(volte)
        if count >= 4000004:
            break
# count = 0
# tempmax = 0
# with open(filename2, 'r', encoding='utf-8') as file_to_read2:
#     while True:
#         count = count + 1
#         lines2 = file_to_read2.readline()  # 整行读取数据
#         if not lines2:
#             break
#         if count >= 5:
#             p_tmp, volte = [float(i) for i in lines2.split(',')]
#             time2.append(p_tmp)
#             voltes2.append((volte-2.5)/0.05)
#         if count >= 32000004:
#             break

fig = plt.figure()
fig2 = plt.figure()
ax = fig.add_subplot(111)
ax2 = fig2.add_subplot(111)
ax.set(xlim=[5, 6], ylim=[0, 6], title='An Example Axes', ylabel='Y-Axis', xlabel='X-Axis')
ax2.set(xlim=[5, 6], ylim=[0, 6], title='An Example Axes', ylabel='Y-Axis', xlabel='X-Axis')
ax.plot(time1, voltes)
# ax2.plot(time2, voltes2)
plt.show()
