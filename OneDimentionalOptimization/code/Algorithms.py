from math import sqrt


def dichotomy(func, a, b, counter, eps, msg=False):
    while b - a > eps:
        mean = (a + b) / 2
        delta = 0.001 * (b - a)
        x1, x2 = mean - delta, mean + delta
        f_x1, f_x2 = func(x1), func(x2)
        counter = counter + 2
        if f_x1 <= f_x2:
            if msg:
                print('next interval [' + str(a) + ',' + str(x2) + ']')
            b = x2
        else:
            a = x1
            if msg:
                print('next interval [' + str(x1) + ',' + str(b) + ']')
    # print('number of requests is ' + Functions.f1_counter)
    res = func((a + b) / 2)
    if msg:
        print('x* = ' + str((a + b) / 2))
        print('f(x*) = ' + str(res))
    return b - a, (a + b) / 2, res


def goldenSection(func, a, b, eps):
    # print(type(func))
    # x1 = a + ((3 - sqrt(5)) / 2) * (b - a)
    # x2 = a + ((sqrt(5) - 1) / 2) * (b - a)
    #print("basic a", func(1/100))
    phi = (1 + sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    f_x1, f_x2 = func(x1), func(x2)
    # print(f_x1,f_x2)
    tau = (sqrt(5) - 1) / 2
    tau = 1/phi
    eps_n = (b - a) / 2
    while eps_n > eps:
        #print("fы" ,f_x1," ",f_x2)
        if f_x1 <= f_x2:
            b = x2
            x2 = x1
            f_x2 = f_x1
            x1 = b - tau * (b - a)
            f_x1 = func(x1)
        else:
            a = x1
            x1 = x2
            f_x1 = f_x2
            x2 = a + tau * (b - a)
            f_x2 = func(x2)
        eps_n = tau * eps_n
    x_min = (a + b) / 2
    #print("min a", func(x_min))
    return x_min


def fibonacciSequence(n):  # TODO переписать через генератор
    if n == 1 or n == 2:
        return 1
    step_1 = 1
    step_2 = 1
    for i in range(2, n):
        tmp = step_2
        step_2 = step_1
        step_1 = tmp + step_2
        # print(step_1)
    return step_1
    # return fibonacciSequence(n - 1) + fibonacciSequence(n - 2)


def fibonacci(func, a, b, n, k, lambd, mu, prev_f, counter, eps, msg=False):
    if k <= n - 2:
        if lambd == float('inf'):
            lambd = a + fibonacciSequence(n - k - 1) / fibonacciSequence(n - k + 1) * (b - a)
            if k != 0:
                f1 = func(lambd)
                counter += 1
                f2 = prev_f
        if mu == float('inf'):
            mu = a + fibonacciSequence(n - k) / fibonacciSequence(n - k + 1) * (b - a)
            if k != 0:
                f1 = prev_f
                f2 = func(mu)
                counter += 1
        if k == 0:
            f1 = func(lambd)
            counter += 1
            f2 = func(mu)
            counter += 1
    else:
        res = func((a + b) / 2)
        if msg:
            print("x* = " + str((a + b) / 2))

            print('f(x*) = ' + str(res))
        # print('number of requests is ' + str(counter))
        return b - a, (a + b) / 2, res

    if f1 > f2:
        prev_f = f2
        if msg:
            print('next interval [' + str(lambd) + ',' + str(b) + ']')
        if k < n - 2:
            return fibonacci(func, lambd, b, n, k + 1, mu, float('inf'), prev_f, counter, eps, msg)
        else:
            return fibonacci(func, lambd, b, n, k + 1, mu, lambd, prev_f, counter, eps, msg)
    else:
        prev_f = f1
        if k < n - 2:
            if msg:
                print('next interval [' + str(a) + ',' + str(mu) + ']')
            return fibonacci(func, a, mu, n, k + 1, float('inf'), lambd, prev_f, counter, eps, msg)
        else:
            if msg:
                print('next interval [' + str(lambd) + ',' + str(b) + ']')
            return fibonacci(func, lambd, b, n, k + 1, mu, lambd, prev_f, counter, eps, msg)
