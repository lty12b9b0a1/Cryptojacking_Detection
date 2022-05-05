import numpy as np
import matplotlib
import matplotlib.pyplot as plt


matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8, 4)

plt.imshow(your_data)

plt.show()
# fig.savefig('eval-overall.pdf')