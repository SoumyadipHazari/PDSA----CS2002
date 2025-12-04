# Computing gcd
#first method is by using list 
''' def gcd(m,n):
    cf = []
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)
    return cf[-1]

print(gcd(16,24)) '''

# without the list
''' def gcd(m,n):
    for i in range (1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            a = i
    return(a)

print(gcd(6,8)) '''

#Eucclid's algorithm beta version
'''def gcd(m,n):
    (a,b) = (max(m,n), min(m,n))
    if a%b == 0:
        return b
    else:
        return (gcd(b,(a-b)))

print(gcd(25,40))'''

#Euclids Algorithm

def gcd(m,n):
    (a,b) = (max(m,n), min(m,n))
    if a%b == 0:
        return b
    else:
        return(gcd(b,(a%b)))
    
print(gcd(35,60))

# 60% 35 == 25 , 35%25 = 10, 25%10 = 15, 15%10 = 5, 10%5 = 0