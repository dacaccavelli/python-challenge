# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:22:03 2018

@author: dcaccavelli
"""

from string import ascii_letters
import re, urllib, webbrowser as wb

wb.open('http://www.pythonchallenge.com/pc/def/%s.html' % join(chr for chr in re.findall(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read(), re.S)[1] if chr in ascii_letters))
