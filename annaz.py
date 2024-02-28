import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(np.pi/2,2*np.pi,10)
x2 = np.linspace(-2*np.pi,np.pi/2,10)
y = np.sin(x)
y2 = np.cos(x)

#выбираем оси
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# вывод двух графиков
plt.plot(x,y, 'b-')
plt.plot(x2,y2, 'b-')
# показ графика
plt.show()