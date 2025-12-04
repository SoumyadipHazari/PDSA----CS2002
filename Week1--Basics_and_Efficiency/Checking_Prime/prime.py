## first approach -- finding out every factor of the number
''' def factor (n):
    fac = []
    for i in range(1,n+1):
        if n%i == 0:
            fac.append(i)
    return (fac)

def prime(n):
    return(factor(n) == [1,n])

a = int(input())

print(prime(a)) '''

## second approach -- directly checking wheather it is prime or not

'''def prime(n):
    result = True
    for i in range(2,n):
        if n % i == 0:
            result = False
    return (result) '''

# third approach -- checking the n//2

'''def prime(n):
    result = True
    for i in range(2,n//2):
        if n%i == 0:
            result = False
    return(result)'''

#fourth approach -- directly breaking the loop whenever the no. is divisable by any number

'''def prime(n):
    result = True
    for i in range(2,n):
        if n%i == 0:
            result = False
            break

    return (result)

a = int(input())
print(prime(a)) '''

#Fifth approach -- checking the factors up to √ n
import math
def prime(n):
    (result,i) = (True,2)
    while (result and (i <= math.sqrt(n))):
        if (n%i) == 0:
            result = False
        i = i+1
    return(result)

a = int(input())
print(prime(a))