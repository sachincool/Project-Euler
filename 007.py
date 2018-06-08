"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

def prime(num):


    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True

found=1
current=3
result=[]

while found<10001:
    if prime(current):
        found+=1
        result.append(current)
    current+=2


print(max(result))

