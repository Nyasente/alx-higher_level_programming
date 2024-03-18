#!/usr/bin/python3
"""
print- retrns all letters except q,e
for: loop iterates over every word
if : loop to check for q,e imposter
"""
for letters in range(ord('a'), ord('z') + 1):
    if letters in (ord('q'), ord('e')):
        continue
    print("{}".format(chr(letters)), end='')
