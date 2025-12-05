# iterative implementation 

'''def bs(m,n):
    low = 0 
    high = len(m)-1
    while low <= high:
        mid = (low+high) // 2
        if m[mid] < n:
            low = mid + 1
        elif m[mid] > n:
            high = mid - 1
        else:
            return mid
        
    return False'''

# recursive implementation without slicing

'''def binarysearch(m,n,high,low):
    if high - low < 0:
        return False
    mid = (high+low) // 2
    if n == m[mid]:
        return mid
    if n > m[mid]:
        return(binarysearch(m,n,mid+1,high))
    else:
        return(binarysearch(m,n,low,mid-1))'''

# lecture implementation
def binarysearch(m,n):
    if m == []:
        return(False)
    mid = len(m)//2
    if n == m[mid]:
        return mid
    if n > m[mid]:
        return(binarysearch(m[mid+1:],n))
    else:
        return(binarysearch(m[:mid],n))