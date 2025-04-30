import matplotlib

matplotlib.use('Qt5Agg')

import numpy as np
import matplotlib.pyplot as plt


print('Введите m:')
m = float(input())

print('Введите k:')
k = float(input())

print('Введите b:')
b = float(input())

print('Введите x0:')
x0 = float(input())

print('Введите V0:')
v0 = float(input())

print('Введите t0:')
t0 = float(input())

print('Введите t1:')
t1 = float(input())

w0 = (k / m) ** 0.5
gamma = b / (2 * m)
w = (w0 ** 2 - gamma ** 2) ** 0.5
A = (x0 ** 2 + ((v0 + gamma * x0) ** 2) / (w ** 2))
fi = -np.arctan((v0 + gamma * x0) / (w * x0))

arr_t = np.array([i for i in np.linspace(t0, t1, 10000)])

arr_x = A * np.exp(-gamma * arr_t) * np.cos(w * arr_t + fi)

plt.plot(arr_t, arr_x)

plt.savefig('plot_task_3_4.png')