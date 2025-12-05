def bs(m,n):
    low = 0
    high = len(m) - 1
    while low <= high:
        mid = (low+high)//2
        if m[mid] < n:
            low = mid+1
        elif m[mid] > n:
            high = mid -1
        else:
            return mid
    return False

def binarysearch(a,b,low,high):
    if high - low < 0:
        return False
    mid = (low + high)//2

    if a[mid] < b:
        return(binarysearch(a,b,mid+1,high))
    else:
        return(binarysearch(a,b,low,mid-1))
    
def linear_search(m,n):
    for i in range (len(m)):
        if n == m[i]:
            return i
    return False



def selection_sort (a):
    n = len(a)
    if n < 1:
        return (a)
    for i in range(n):
        minpos = i
        for j in range (i+1,n):
            if a[j] < a[minpos]:
                minpos = j
        (a[i],a[minpos]) = (a[minpos],a[i])
    return (a)

def insertion_sort(b):
    m = len(b)
    if m < 1:
        return b
    for i in range(m):
        j = i
        while j > 0 and b[j] < b[j-1]:
            (b[j],b[j-1]) = (b[j-1],b[j])
            j = j - 1
    return b