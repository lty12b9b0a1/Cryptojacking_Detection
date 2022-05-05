import matplotlib.pyplot as plt
# import numpy as np
filename = './data/nbminer.csv'
filename2 = './data/gminer.csv'
filename3 = './data/phoenixminer.csv'
filename4 = './data/bminer.csv'
filename5 = './data/1.20/4096-128cudacore.csv'
pos = []
time1 = []
time2 = []
time3 = []
time4 = []
time5 = []

voltes = []
voltes2 = []
voltes3 = []
voltes4 = []
voltes5 = []
tempmax = 0
count = 0
with open(filename, 'r', encoding='utf-8') as file_to_read:
    while True:
        count = count + 1
        lines = file_to_read.readline()  # 整行读取数据
        if not lines:
            break
        if count >= 5:
            p_tmp, volte = [float(i) for i in lines.split(',')]
            time1.append(p_tmp)
            voltes.append(volte)
        if count >= 3200004:
            break
count = 0
tempmax = 0
with open(filename2, 'r', encoding='utf-8') as file_to_read2:
    while True:
        count = count + 1
        lines2 = file_to_read2.readline()  # 整行读取数据
        if not lines2:
            break
        if count >= 5:
            p_tmp, volte = [float(i) for i in lines2.split(',')]
            time2.append(p_tmp)
            voltes2.append(volte)
        if count >= 32000004:
            break


count = 0
tempmax = 0
with open(filename3, 'r', encoding='utf-8') as file_to_read3:
    while True:
        count = count + 1
        lines3 = file_to_read3.readline()  # 整行读取数据
        if not lines3:
            break
        if count >= 5:
            p_tmp, volte = [float(i) for i in lines3.split(',')]
            time3.append(p_tmp)
            voltes3.append(volte)
        if count >= 32000004:
            break


count = 0
tempmax = 0
with open(filename4, 'r', encoding='utf-8') as file_to_read4:
    while True:
        count = count + 1
        lines4 = file_to_read4.readline()  # 整行读取数据
        if not lines4:
            break
        if count >= 5:
            p_tmp, volte = [float(i) for i in lines4.split(',')]
            time4.append(p_tmp)
            voltes4.append(volte)
        if count >= 32000004:
            break


count = 0
tempmax = 0
with open(filename5, 'r', encoding='utf-8') as file_to_read5:
    while True:
        count = count + 1
        lines5 = file_to_read5.readline()  # 整行读取数据
        if not lines5:
            break
        if count >= 5:
            p_tmp, volte = [float(i) for i in lines5.split(',')]
            time5.append(p_tmp)
            voltes5.append(volte)
        if count >= 32000004:
            break


fig = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
fig4 = plt.figure()
fig5 = plt.figure()
ax = fig.add_subplot(111)
ax2 = fig2.add_subplot(111)
ax3 = fig3.add_subplot(111)
ax4 = fig4.add_subplot(111)
ax5 = fig5.add_subplot(111)
ax.set(xlim=[5, 6], ylim=[2.4, 3], title='--', ylabel='Y-Axis', xlabel='X-Axis')
ax2.set(xlim=[5, 6], ylim=[2.4, 3], title='--', ylabel='Y-Axis', xlabel='X-Axis')
ax3.set(xlim=[5, 6], ylim=[2.4, 3], title='--', ylabel='Y-Axis', xlabel='X-Axis')
ax4.set(xlim=[5, 6], ylim=[2.4, 3], title='--', ylabel='Y-Axis', xlabel='X-Axis')
ax5.set(xlim=[5, 6], ylim=[2.4, 3], title='--', ylabel='Y-Axis', xlabel='X-Axis')
ax.plot(time1, voltes)
ax2.plot(time2, voltes2)
ax3.plot(time3, voltes3)
ax4.plot(time4, voltes4)
ax5.plot(time5, voltes5)
plt.show()
