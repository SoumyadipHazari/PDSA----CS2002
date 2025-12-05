def f(n):
    s = 0
    for i in range(2,n):
        if n % i == 0 and i % 2 == 1:
            s = s + 1
    return(s)