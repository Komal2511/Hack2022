# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:02:09 2022

@author: Komal And Omkar
"""

# Python program to check if the number is an Armstrong number or not
# An Armstrong number is one whose sum of digits raised to the power three equals the number itself.
# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
