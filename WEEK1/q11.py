def fun(n):
    if n == 0:
        return 0
    return (n % 10) + fun(n//100)