def selectionsort(m):
    n = len(m)
    if n < 1:
        return(m)
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if m[j] < m[minpos]:
                minpos = j
        (m[i],m[minpos]) = (m[minpos],m[i])
    return (m)
