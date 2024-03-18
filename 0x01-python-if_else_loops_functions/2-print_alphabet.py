#!/usr/bin/python3
'''
Prints alphabet letters in lowercase.
For: A loop to print all the ASCII characters in lowercase.
'''
for char in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(char)), end='')
