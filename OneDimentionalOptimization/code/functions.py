from math import exp, sin


class Functions:
    f1_counter = 0
    f2_counter = 0

    @staticmethod
    def f1(x):
        Functions.f1_counter += 1
        return x ** 2 - 2 * x + exp(-x)

    @staticmethod
    def f2(x):
        Functions.f2_counter += 1
        return x ** 3 - 3 * sin(x)
