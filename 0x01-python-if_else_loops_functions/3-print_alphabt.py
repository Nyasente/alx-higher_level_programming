#!/usr/bin/python3
"""
print- retrns all letters except q,e
for: loop iterates over every word
if : loop to check for q,e imposter
"""
for letters in range (97,123):
    if letters in [101, 113]:
        continue
    print("{}".format(chr(letters)), end='')
