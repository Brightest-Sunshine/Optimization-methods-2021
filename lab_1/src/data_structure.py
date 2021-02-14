import numpy as np


class CanonicalForm:
    """
    Класс, хранящий входные данные канонической формы задачи линейного программирования.
    Обозначения переменных: пособие Петухова и др., стр. 80, ф.-ла (4.25)
    """

    def __init__(self, A, b, c):
        self.n = len(c)
        self.m = len(b)
        dimensions_matched = len(A) == self.m
        for row in A:
            dimensions_matched &= len(row) == self.n
        if not dimensions_matched:
            raise Exception("dimensions mismatch")
        self.A, self.b, self.c = A, b, c


class NpCanonicalForm:
    """
    Представление канонической формы в виде массивов NumPy (в отличие от списков в `CanonicalForm`)
    """

    def __init__(self, cf: CanonicalForm):
        self.n, self.m = cf.n, cf.m
        self.A = np.array([np.array(row) for row in cf.A])
        self.b = np.array(cf.b)
        self.c = np.array(cf.c)
