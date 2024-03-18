#!/usr/bin/python3
"""
print- retrns all letters except q,e
for: loop iterates over every word
if : loop to check for q,e imposter
"""
for letters in range(ord('a'), ord('z') +1):
    letters = chr(letters)
    if letters not in "q,e":
        print(letters, end='')
