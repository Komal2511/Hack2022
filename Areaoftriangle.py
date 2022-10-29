# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:00:37 2022

@author: Komal and Omkar
"""

# Python Program to find the area of triangle

a = 14
b = 9
c = 18

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
