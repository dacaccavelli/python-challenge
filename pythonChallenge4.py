# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:24:56 2018

@author: dcaccavelli
"""
# Scrape web pages for the following page until the final page in the
# list is reached.

import urllib.request

# Starting page id.
next_page = [12345]

for i in range(0, 400):

    with urllib.request.urlopen(
      'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' %
      next_page[0]) as response:

        html = response.read()
        # Needed for request to "divide by two" on page 16044.
        if next_page[0] == 16044:
            next_page[0] = 8022
        else:
            next_page = [int(s) for s in html.split() if s.isdigit()]
            # Catching end of chain to break the loop.
            if next_page:
                print(next_page[0])
            else:
                break


# answer is peak.html
