#!/bin/python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def primeNumber(num):
  primes = [2,3]
  counter = 2
  flag = True
  i=5
  while counter < num:
    check = True
    j=1
    while j < len(primes) and check:
      if i%primes[j] == 0:
        check = False
      j+=1
    if check:
      primes.append(i)
      counter+=1
    i+=2
  return primes

print primeNumber(10001)
