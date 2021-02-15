# Функции для создания двойственной задачи


def check_signs(A, b, MatrixSigns):
    for i in range(len(MatrixSigns)):
        if MatrixSigns[i] == "<=":
            for j in range(len(A[i])):
                A[i][j] = -A[i][j]
            b[i] = -b[i]
            MatrixSigns[i] = ">="


def transpose_matrix(A):
    B = []
    for _ in range(len(A)):
        B.append([])
    for i in range(len(A)):
        for j in range(len(A[i])):
            B[j].append(A[i][j])
    return B


def new_vector(c):
    return c


def new_coeff(b):
    return b


def new_mtrx_signs(VariablesSigns):
    signs = []
    for i in range(len(VariablesSigns)):
        if VariablesSigns[i] == ">=":
            signs.append(">=")
        elif VariablesSigns[i] == "":
            signs.append("=")
    return signs


def new_var_signs(MatrixSigns):
    signs = []
    for i in range(len(MatrixSigns)):
        if MatrixSigns[i] == ">=":
            signs.append(">=")
        elif MatrixSigns[i] == "=":
            signs.append("")
    return signs


def new_function(func):
    if func == "min":
        return "max"
    return "min"
