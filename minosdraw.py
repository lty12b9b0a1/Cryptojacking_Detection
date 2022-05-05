import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import math

dataff = []
file_names = ["./binary_obfus/ethminer.exe",
              "./binary_obfus/enigma/weak/ethminer.exe",
              "./binary_obfus/upx/level1/ethminer.exe",
              "./binary_obfus/upx/level9/ethminer.exe",
              ]
for file_name in file_names:
    dataf = np.array([])
    dataf = np.resize(dataf, (0, 100, 100, 1))
    targetf = np.array([])
    targetf = np.resize(targetf, (0, 1))

    file_stats = os.stat(file_name)
    ln = file_stats.st_size
    ln = math.floor(ln/256)
    width = math.floor(pow(ln, 0.5))
    a = np.fromfile(file_name, dtype='uint16', count=width * width)
    g = a.reshape(-1, 1)
    g = g / 65535
    # g = np.log2(g)
    g = g.reshape(-1, width, 1)
    # data = np.array([i for i in g])
    # dataf = np.concatenate((dataf, data), axis=0)

    # dataf = dataf.reshape(-1, 100, 1)
    dataff.append(g)


matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8, 2.8)

ax1 = fig.add_subplot(141)
ax1.set(xlabel='Origin\n(3387KB)')
ax1.set_xticks([], [])
ax1.set_yticks([], [])
ax2 = fig.add_subplot(142)
ax2.set(xlabel='Enigma\n(3256KB)')
ax2.set_xticks([], [])
ax2.set_yticks([], [])
ax3 = fig.add_subplot(143)
ax3.set(xlabel='UPX-weak\n(1680KB)')
ax3.set_xticks([], [])
ax3.set_yticks([], [])
ax4 = fig.add_subplot(144)
ax4.set(xlabel='UPX-strong\n(1223KB)')
ax4.set_xticks([], [])
ax4.set_yticks([], [])
# ax5 = fig.add_subplot(235)
# ax6 = fig.add_subplot(236)
# ax7 = fig.add_subplot(247)
# ax8 = fig.add_subplot(248)
ax1.imshow(dataff[0], cmap=plt.cm.gist_gray, aspect="auto", vmin=0, vmax=1)
ax2.imshow(dataff[1], cmap=plt.cm.gist_gray, aspect="auto", vmin=0, vmax=1)
ax3.imshow(dataff[2], cmap=plt.cm.gist_gray, aspect="auto", vmin=0, vmax=1)
ax4.imshow(dataff[3], cmap=plt.cm.gist_gray, aspect="auto", vmin=0, vmax=1)
# ax5.imshow(dataff[4], cmap=plt.cm.Greys, aspect="auto", vmin=0, vmax=1)
# ax6.imshow(dataff[5], cmap=plt.cm.Greys, aspect="auto", vmin=0, vmax=1)
# ax7.imshow(dataff[6], cmap=plt.cm.Greys, aspect="auto", vmin=0, vmax=1)
# ax8.imshow(dataff[7], cmap=plt.cm.Greys, aspect="auto", vmin=0, vmax=1)
# plt.colorbar()
plt.show()
