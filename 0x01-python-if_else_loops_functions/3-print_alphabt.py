#!/usr/bin/python3
"""
print- ascii for a to z excluding q and e
"""
for alphabet in range(97, 123):
    if alphabet not in (101, 113):
        print (chr(alphabet), end='')
