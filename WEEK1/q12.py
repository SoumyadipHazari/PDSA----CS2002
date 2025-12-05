def fun(n):
    if n == 0:
        return 0
    if (n % 10) % 2 == 0:
        return 1 + fun(n // 10)
    else:
        return fun(n // 10)