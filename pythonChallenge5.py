# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:51:55 2018

@author: dcaccavelli
"""
# Importing and decoding a pickle file. Using the tuples listed within,
# join the characters as described to create the message.

from urllib.request import urlopen
import pickle

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for line in data:

    print("".join([k * v for k, v in line]))

# answer is channel
