from GradientMethods.code.functions import Function
from OneDimentionalOptimization.code.Algorithms import goldenSection
import matplotlib as mpl
import math


def draw_line(ax, x1, x2):
    l = mpl.lines.Line2D([x1[0], x2[0]], [x1[1], x2[1]])
    l.set_marker("o")
    ax.add_line(l)


def additional_function(x, gradient):
    # for i in range(len(x)):
    #     x[i] -= alpha * gradient[i]
    # x -= alpha*gradient
    def inner(a):
        new_x = []
        for i in range(len(x)):
            new_x.append(x[i] - a * gradient[i])
        return Function.F(new_x[0], new_x[1])

    return inner


def norm(x, p):
    if p == 'inf':
        max_x = 0
        for x_i in x:
            if abs(x_i) > max_x:
                max_x = abs(x_i)
        return max_x

    summary = 0
    for x_i in x:
        summary += abs(pow(x_i, p))
    return pow(summary, 1 / p)


def Quickest_descent(function, eps, x, ax, alpha=0, p=2):
    gradient = Function.gradient(x)
    count = 0
    delta_x = 10
    counts = []
    norms = []
    while norm(gradient, p) >= eps:
        count += 1
        # print("norm:", norm(gradient, 2))
        new_func = additional_function(x, gradient)
        if count == 0:
            values = [eps, eps / 2, eps / 10, eps / 100, eps / 125, eps / 250]
        else:
            values = [eps / 125]
        for val in values:
            alpha = goldenSection(new_func, 1 / 250, 1, val)
            # print("a ", alpha)
            old_x = x.copy()
            for i in range(len(x)):
                x[i] -= alpha * gradient[i]
            draw_line(ax, old_x, x)
            del_norm = norm([x[0] - old_x[0], x[1] - old_x[1]], 2)
            # print(del_norm)
            # print(val, del_norm)
            #print(val, Function.F(x[0], x[1]))
            counts.append(count)
            norms.append(del_norm)
            if del_norm < delta_x:
                delta_x = del_norm
        print("x_k", x)
        print("f(x_k)", Function.F(x[0], x[1]))
        gradient = Function.gradient(x)
    # print(norms)
    # print(counts)
    # print(eps, count)
    # print(eps,delta_x)
    return x


if __name__ == '__main__':
    result = additional_function([1, 1], 2)
    print(result)
