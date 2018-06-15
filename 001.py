"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

print(sum(x for x in range(1000) if (x%3==0 or x%5==0)))

// Better Approach 
 n = int(input().strip())-1
    n1=n//3
    n1=3*n1*(n1+1)//2
    n2=n//5
    n2=5*n2*(n2+1)//2
    n3=n//15
    n3=15*n3*(n3+1)//2
    print (n1+n2-n3)
