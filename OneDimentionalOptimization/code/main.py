from OneDimentionalOptimization.code.functions import *
from OneDimentionalOptimization.code.Algorithms import dichotomy, fibonacciSequence, fibonacci
from OneDimentionalOptimization.code.graphics import plotFunctions

EPSILON = 0.05
EPSILONS = [0.1, 0.01, 0.001]
LEFT_BOARDER = 1
RIGHT_BOARDER = 1.5


def run_dichotomy(eps, func, msg=False):
    f1 = func
    plotFunctions(f1, LEFT_BOARDER, RIGHT_BOARDER)
    Functions.reset_counters()
    # print(Functions.f1_counter)
    count = 0
    interval, x_min, f_min = dichotomy(f1, LEFT_BOARDER, RIGHT_BOARDER, count, eps, msg)
    ration = interval / (RIGHT_BOARDER - LEFT_BOARDER)
    if msg:
        print('Dichotomy method')
        print('start interval [' + str(LEFT_BOARDER) + ',' + str(RIGHT_BOARDER) + ']')
        print('number of requests is ' + str(Functions.f1_counter - 1))
        print('compression ration is ' + str((interval / (RIGHT_BOARDER - LEFT_BOARDER))))
        print()

    return f_min, ration


def run_fib(eps, func, msg=False):
    f1 = func
    #N = (RIGHT_BOARDER - LEFT_BOARDER) / eps
    N = 7
    n = 1
    count = 0
    while fibonacciSequence(n) < N:  # TODO переделать
        n = n + 1
    interval, x_min, f_min = fibonacci(f1, LEFT_BOARDER, RIGHT_BOARDER, n, 0, float('inf'), float('inf'), float('inf'),
                                       count, eps, msg)
    ration = interval / (RIGHT_BOARDER - LEFT_BOARDER)
    # print(interval)
    if msg:
        print('Fibonacci method')
        print('start interval [' + str(LEFT_BOARDER) + ',' + str(RIGHT_BOARDER) + ']')
        print('number of requests is ' + str(Functions.f1_counter - 1))

        print('compression ration is ' + str(ration))
    return f_min, ration


if __name__ == '__main__':
    print("Для функции x ** 2 - 2 * x + exp(-x)")
    print("dichotomy")
    for eps in EPSILONS:
        res, rat = run_dichotomy(eps, Functions.f1)
        print(eps, " | ", res, " | ", Functions.f1_counter - 1, " | ", rat)
        Functions.reset_counters()
    print("fibonacci")
    for eps in EPSILONS:
        res, rat = run_fib(eps, Functions.f2)
        print(eps, " | ", res, " | ", Functions.f2_counter - 1, " | ", rat)
        Functions.reset_counters()
    LEFT_BOARDER = 0.5
    RIGHT_BOARDER = 1
    print("Для функции x ** 3 - 3 * sin(x)")
    print("dichotomy")
    for eps in EPSILONS:
        res, rat = run_dichotomy(eps, Functions.f1)
        print(eps, " | ", res, " | ", Functions.f1_counter - 1, " | ", rat)
        Functions.reset_counters()
    print("fibonacci")
    for eps in EPSILONS:
        res, rat = run_fib(eps, Functions.f2)
        print(eps, " | ", res, " | ", Functions.f2_counter - 1, " | ", rat)
        Functions.reset_counters()
    run_fib(EPSILON, Functions.f1, msg = True)