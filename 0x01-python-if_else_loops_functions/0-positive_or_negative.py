#!/usr/bin/python3
'''
import - a module with some functions
print: returns positive or negative or zero on success
'''
import random
number = random.randint(-10, 10)
if number > 0:
    print(number, 'is positive')
if number == 0:
    print(number, 'is zero')
if number < 0:
    print(number, 'is negative')
