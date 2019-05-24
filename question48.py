#!/usr/bin/env python3

# Self powers
#Problem 48
#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000

result = 0

for num in range(1,1001):
  result+= num**num

print(result % 10000000000)


# 9110846700 YAY

