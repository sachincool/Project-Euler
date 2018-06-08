"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

x=1000
for a in range(1,x+1):
    for b in range(2,x+1):
        if (a>b):
            continue
        if a+b+(a**2+b**2)**0.5==x:
            print (int(a*b*(a**2+b**2)**0.5))

