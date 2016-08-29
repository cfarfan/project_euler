#!/bin/python
# -*- coding: utf-8 -*-

# The sum of the squares of the first ten natural numbers is,

# 12^2 + 22^2 + ... + 102^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def sumSquareDifference(num):
  sum_sqr = 0
  sqr_sum = 0
  for i in xrange(1,num+1):
    sum_sqr += pow(i,2)
    sqr_sum += i
  sqr_sum = pow(sqr_sum,2)
  return sqr_sum-sum_sqr

n = 100
print 'Result for:',n,'is',sumSquareDifference(n)
