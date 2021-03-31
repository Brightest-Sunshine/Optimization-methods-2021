import math


class Function:
    counter = 0

    @staticmethod
    def reset_counter():
        Function.counter = 0

    @staticmethod
    def F(x, y):
        Function.counter += 1
        return 2 * x ** 2 + y ** 2 + math.cos(6 * x + 5 * y) - x + 2 * y

    @staticmethod
    def dF_dx(x, y):
        return 4 * x - 6 * math.sin(6 * x + 5 * y) - 1

    @staticmethod
    def dF_dy(x, y):
        return 2 * y - 5 * math.sin(6 * x + 5 * y) + 2

    @staticmethod
    def gradient(X):
        return [Function.dF_dx(X[0], X[1]), Function.dF_dy(X[0], X[1])]