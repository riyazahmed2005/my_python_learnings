# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 19:56:13 2023
pg.no 14
28.4.2023
Find Sum and Product of two-digit number
@author: Riyaz
"""

a = int(input("Enter the number: "))

q = a // 10
r = a % 10

sum = q + r
p = q * r

print(sum)
print(p)