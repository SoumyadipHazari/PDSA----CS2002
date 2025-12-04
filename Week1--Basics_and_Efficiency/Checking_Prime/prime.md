# Finding Prime number 
let 1 is not a prime number as it has only one divisor i.e; 1

### First way storing the factors 

    def factor(n):
        fac = []
        for i in range(1,n+1):
            if n % i == 0:
                fac.append(i)
        return (fac)

    def prime(n):
    return(factor(n) == [1,n]) 

here what we are doing is finding out the factors of the no. 'n' by dividing 1 to n to n and then we are storing the factors in a list and we are comparing the list with the [1,n].

### Second way is to directly check whether it is prime or not

    def factor (n):
        result = True
        for i in range(2,n):
            if n % i == 0:
                result = False
        return (result)

here we are not storing the factors rather we are approaching in a direct way by starting the divison by 2 (as we all know that a every no. is divisable 1) and dividing upto n-1 (as the no. is divisable by that no. itself) and if it is divisable by any no. other that 1 and n then it is not prime and we  decalre the result as 'False'

### Third way is to check if n has any factor between 2 and n//2

    def factor(n):
        result = True
        for i in range (2, n//2):
            if n % i == 0:
                result = False
        return (result)

It is similiar to the Second method but here we are checking if any factor of n is present from 2 to n//2.

it just  decreases the range of checking 

### Fourth way is to terminate the loop when we find the first factor between 2 and n 

    def factor(n):
        result = true
            for i in range (2,n):
                if n % i == 0:
                    result = False 
                    break
            return (result)

here we are terminating the loop as soon as we find a factor other than 1 or n so we don't need to go through the every number till n-1

### Fifth way is to check factors up to √ n

    import math
    def prime(n):
        (result,i) = (true,2)
        while (result and (i <= math.sqrt(n))):
            if (n%i) == 0:
                result = False
            i = i+1
        return (result)

1. Initialization
   
        (result, i) = (True, 2)

- result = True --> assume n is prime until proven otherwise
- i = 2 --> start checking divisibility from 2

2. Loop condition
    
        while result and (i <= math.sqrt(n)):

The loops runs until
- the result stays true 
- i is less than or equal to √ n

3. Why only upto √ n
- If n has a factor larger than \sqrt{n}, the corresponding smaller factor would already have been found.


The time complexity is O(√n)
