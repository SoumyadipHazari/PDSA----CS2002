def merge(a,b):
    (x,y) = (len(a),len(b))
    (c,i,j) = ([],0,0)

    while i < x and j < y:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < x:
        c.append(a[i])
        i += 1

    while j < y:
        c.append(b[j])
        j +=1

    return c

def mergesort (l):
    n = len(l)
    if n <= 1:
        return(l)
    left_half = mergesort(l[: n//2])
    right_half = mergesort(l[n//2 :])
    sorted_merged_list = merge(left_half,right_half)
    return(sorted_merged_list)