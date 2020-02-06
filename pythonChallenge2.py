# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:22:21 2018

@author: dcaccavelli
"""
# Searching text doc for characters that appear only once.
file = open(r"pythonChallenge2.txt", "r")
myDict = {}
for char in file.read():
    if char in myDict.keys():
        myDict[char] += 1
    else:
        myDict[char] = 1

print(myDict)
file.close()

# answer is equality
