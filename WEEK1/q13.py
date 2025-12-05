def fun(n):
    if n <= 1:
        return 0
    return fun(n - 1) + fun(n - 2)

fun(5)