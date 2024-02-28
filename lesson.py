# построение графика
fig, ax = plt.subplots()
ax.set_title('График')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.ylim(-100, 100)

if (a < 0 and b > 0) or (a > 0 and b < 0):
    x1 = np.linspace(a, 0)
    x2 = np.linspace(0, b)

    ax.plot(x1, math.cos(x1))
    ax.plot(x2, math.cos(x2))
else:
    x = np.linspace(a, b)

    ax.plot(math.cos(x))