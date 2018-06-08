"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
a = 600851475143
b = 2

while b ** 2  < a:
     if a % b == 0:
         a = a / b
     b = b + 1

print (int(a))
