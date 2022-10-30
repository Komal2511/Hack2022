# -*- coding: utf-8 -*-
"""
@author: Komal and Omkar
"""

# Python program to check if year is a leap year or not

year = 1999

# To get year (integer input) from the user
# y = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (y % 400 == 0) and (y % 100 == 0):
    print("{0} is a leap year".format(y))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (y % 4 ==0) and (y % 100 != 0):
    print("{0} is a leap year".format(y))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(y))
