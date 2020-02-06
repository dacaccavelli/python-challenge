# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:08:59 2018

@author: dcaccavelli
"""
# input string to change decode
string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."  # noqa
newstring = ""

for char in string:

    # Preserving punctuation.
    if char < "a":
        newchar = char
    # Advancing each char by two because that is the given clue.
    else:
        code = ord(char)
        code += 2
        if code >= 123:
            code = code % 123 + 97

        newchar = chr(code)

    newstring += newchar

print(newstring)

# answer is ocr
