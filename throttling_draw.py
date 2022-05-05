import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import xlrd
filenames = ["D:/Desktop/1080ti.xls",
             "D:/Desktop/1070.xls",
             "D:/Desktop/2060.xls",
             "D:/Desktop/3060ti.xls",
             ]
gpunames = ["GTX 1080ti",
            "GTX 1070",
            "RTX 2060",
            "RTX 3060ti",
            ]
matplotlib.rcParams.update({'font.size': 16})
fig, axes_l = plt.subplots(nrows=1, ncols=4, sharey=True)
fig.set_size_inches(8, 4.8)

for i, ax in enumerate(axes_l):

    readbook = xlrd.open_workbook(filenames[i])
    sheet = readbook.sheet_by_name('load')
    data = []
    for m in range(4):
        for n in range(4):
            data.append(sheet.cell(m+1, n+1).value)
    dataf = np.array([1-i/100 for i in data])
    dataf.resize(4, 4)
    if i == 0:
        ax.set_ylabel('Inactive Time')
    ax.set_xlabel('Active Time')
    ax.set_xticks([], [])
    ax.set_yticks([], [])

    im = ax.imshow(dataf, cmap='GnBu')
    ax.set_title(gpunames[i], fontsize=16)
# shared colorbar for left subfigure
clb = plt.colorbar(im, ax=axes_l, location='bottom', fraction=0.05, pad=0.08)
clb.ax.set_title('Throttling Rate', fontsize=16)
# clb.ax.set_xticks([],[])
# clb.ax.xaxis.tick_top()
plt.show()