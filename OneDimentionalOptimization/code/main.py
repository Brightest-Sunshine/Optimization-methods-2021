from OneDimentionalOptimization.code.functions import *
from OneDimentionalOptimization.code.Algorithms import dichotomy, fibonacciSequence, fibonacci
from OneDimentionalOptimization.code.graphics import plotFunctions

EPSILON = 0.05
LEFT_BOARDER = 1
RIGHT_BOARDER = 1.5

if __name__ == '__main__':
    f1 = Functions.f1
    plotFunctions(f1, LEFT_BOARDER, RIGHT_BOARDER)

    count = 0
    print('Dichotomy method')
    interval = dichotomy(f1, LEFT_BOARDER, RIGHT_BOARDER, count, EPSILON)
    print('compression ration is ' + str((RIGHT_BOARDER - LEFT_BOARDER) / interval))
    print()
    print('Fibonacci method')
    print('start interval [' + str(LEFT_BOARDER) + ',' + str(RIGHT_BOARDER) + ']')

    count = 0
    N = (RIGHT_BOARDER - LEFT_BOARDER) / EPSILON
    n = 1
    while fibonacciSequence(n) < N:
        n = n + 1
    interval = fibonacci(f1, LEFT_BOARDER, RIGHT_BOARDER, n, 0, float('inf'), float('inf'), float('inf'), count,
                         EPSILON)
    print(interval)
    print('Вызовов f1', Functions.f1_counter)
    ration = (RIGHT_BOARDER - LEFT_BOARDER) / interval
    print('compression ration is ' + str(ration))
