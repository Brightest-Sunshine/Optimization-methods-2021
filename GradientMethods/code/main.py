from FirstOrderMethod import Quickest_descent as qd
import numpy as np
import matplotlib.pyplot as plt
from functions import Function
import matplotlib as mpl

if __name__ == '__main__':
    print('Hello World!')
    first_x = [2.5,-3]#[0,2.5]#[2,-3.5]#[-3,1.5]#[2.5, 0.6]
    eps = 1e-4
    fig, ax = plt.subplots()
    result = qd(eps, eps, first_x, ax)
    x, y = np.meshgrid(np.arange(-4, 4, 0.005), np.arange(-4, 4, 0.005))
    z = 2 * x ** 2 + y ** 2 + np.cos(6 * x + 5 * y) - x + 2 * y
    # 2 * x ** 2 + y ** 2 + math.cos(6 * x + 5 * y) - x + 2 * y

    #  Задаем значение каждого уровня:
    lev = [0, 1, 2, 3, 4, 6, 10, 20, 40, 100, 900, 10000]

    #  Создаем массив RGB цветов каждой области:
    color_region = np.zeros((12, 3))
    color_region[:, 1:] = 0.2
    color_region[:, 0] = np.linspace(0, 1, 12)
    ax.contourf(x, y, z, levels=25)  # , colors=color_region)

    fig.set_figwidth(10)  # ширина и
    fig.set_figheight(10)  # высота "Figure"

    plt.show()
    #plt.savefig('eps_0.jpg')
    # print(Function.gradient([0.2574299749411413, -0.9805968069037432]))
    # print(Function.F(0.44633564, -1.16025564))
    # epss = [1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9]
    # for eps in epss:
    #     first_x = [-2, 2.7]
    #     result = qd(eps, eps, first_x, ax)
    # p = [1, 2, 3, 5, 10,15,20, 'inf']
    # for pp in p:
    #     first_x = [-2, 2.7]
    #     result = qd(eps, eps, first_x, ax, p=pp)
    #     print(pp,result)
