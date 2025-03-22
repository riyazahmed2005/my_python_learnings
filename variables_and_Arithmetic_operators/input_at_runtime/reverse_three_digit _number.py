# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 
pg.no 15
29.4.2023
Reverse the three digit number
@author: Riyaz
"""

a = int(input("Enter the value of a: "))

q = a // 10
r = a % 10
x = q // 10
y = q % 10

reverse = r * 100 + y * 10 + x

print(reverse)