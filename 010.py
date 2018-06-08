"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
 
def sumOfPrimes(limit):
    a = [True] * limit
    a[0]=a[1]=False

    for counter, candidate in enumerate(a):
        if not counter % 2:
            a[counter] = False
        if candidate:
            yield counter
            for n in range(counter**2, limit, counter): 
                a[n] = False
print(sum(list(sumOfPrimes(2*10**6))))
