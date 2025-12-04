# Finding Greatest Common Diviser

let gcd(8,12) -- 
- factors of 8 -- 1,2,4,8
- factors of 12 -- 1,2,3,4,6,12
    
so Common factors are -- 1,2,4

so the gcd(8,12) = 4

so to coumpute the greatest common divisor we will first use the list method --

    def gcd(m,n):
    factor = []
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            factor.append(i)
    return factor[-1]

In the first method we are using a list (ex - factor) to store the common factors beween m and n and the last element of the list is returned as the greatest common factor

line by line explanation -- 
    
    def gcd(m,n)

A function is defined named as gcd where two variables are stored m,n like if we try to find greatest common factor of 24 and 40 then m will store 24 and n will 40 

    factor = []

a empty list is declared where we will store all the common factors between m and n

    for i in range(1, min(m,n)+1):

a for loop is declared  where the range is 1 to min(m,n)+1.

**Why min(m,n)??** -- let we need to find gcd between 15 and 40 then of course 16 or 20 will not be the common factor between 15 and 40 as it is greater than the 15 so we always need to take the range <= the lowest number

    if (m%i) == 0 and (n%i) == 0:

we will iterate to every number till the smallest number of the given two numbers and check wheatherthey divide both the no. or not

    factor.append(i)

if it divides the both the m and n then the no. will be appended to the list

    return factor[-1]

then we will return the last element of the factor list. and it will be the greatest common diviser

### Without using the list --

    def gcd(m,n):
    for i in range (1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            a = i
    return(a)

same process we are just excluding the list from the process and returning the last no. which divides the both number as the greatest common divisor of m and n.

### Finding GCD uing better way 

    def gcd(m,n):
    (a,b) = (max(m,n), min(m,n))
    if a%b == 0:
        return b
    else:
        return (gcd(b,(a-b)))

here we are not using list and also the iteration.
suppose d divides both 'm' and 'n' then m = ad and n = bd
m - n = (a-b)d then d also divides m - n 

all the things are same but in the last line 
    
    return gcd(b, a - b)

here by substracting 'a-b' we are preserving the gcd
let we want to find out the  gcd of (18,24) then 

gcd(18,24)
- gcd(18, (24-18)) -- gcd(18,6)
- gcd(6, (18-6)) -- gcd(6,12)
- gcd(6, (12-6)) -- gcd(6, 6)
- gcd(6,6) --> return gcd = 6

then lets think that we need to find out the gcd of (1,1000) then we need to make 1000 recursive calls, almost like counting down 999, 998, 997…

that's when Euclid's algorithm comes in handy --

    def gcd(m,n):
        (a,b) = (max(m,n), min(m,n))
        if a%b == 0:
            return b
        else:
            return(gcd(b,(a%b)))

here everything is same just last line is changed where before we are using (a-b) and now we are using (a%b)

**why euclid's algorithm is faster?**

let we wanted to find the gcd of (18,24) then by doing (b, (a-b)) we need to make many recursive calls while if you do (b, (a%b)) where
- gcd(18,24) --> gcd(18, (24%18))
- gcd (18,6) --> gcd(6, (18%6))
- returns gcd --> 6 


