import numpy as np
import matplotlib.pyplot as plt


def np_func(func, array):
    y = []
    for i in array:
        y.append(func(i))
    return y


def plotFunctions(func, a, b):
    x = np.arange(a, b, 0.01)
    y = np_func(func, x)
    plt.title('График функции', fontsize=13)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(x, y, label='x^2 - 2x + e^(-x)', linewidth=0.8, color='darkblue')
    plt.legend()
    plt.show()
    return
