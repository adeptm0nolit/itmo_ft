import matplotlib

matplotlib.use('Qt5Agg')


import matplotlib.pyplot as plt


with open('./CdSe_CdZnS Core_Shell.txt') as f:
    f = f.readlines()

x = []
y = []
for i in f:
    i = list(map(float, i.replace(',', '.').split('\t')))
    if len(i) == 2:
        x.append(float(i[0]))
        y.append(float(i[1]))
    else:
        continue

plt.plot(x, y)
plt.show()