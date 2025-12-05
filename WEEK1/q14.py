def fun(n):
    if n <= 1:
        return 0
    if n % 2 == 0:
        return fun(n // 2)
    else:
        return 1 + fun(n // 2) + fun(n // 2)

fun(18)