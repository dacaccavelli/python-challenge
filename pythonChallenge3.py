# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:15:33 2018

@author: dcaccavelli
"""
# Searching for lower case characters surrounded by exactly three upper
# case characters on either side. Could be replaced by regex.

file = open("pythonChallenge3.txt", "r")
fileArray = []
counter = 0
stored = ""
finalStored = ""

# Save list into array.
for char in file.read():
    fileArray.append(char)
file.close()

for i in range(4, len(fileArray)):
    # Checking local characters for correct case.
    if(fileArray[i-4].islower() and
       fileArray[i-3].isupper() and
       fileArray[i-2].isupper() and
       fileArray[i-1].isupper() and
       fileArray[i].islower() and
       fileArray[i+1].isupper() and
       fileArray[i+2].isupper() and
       fileArray[i+3].isupper() and
       fileArray[i+4].islower()):
        finalStored += fileArray[i]

print(finalStored)

# answer is linkedlist
