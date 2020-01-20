# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_301268.html (Sum ends with 16)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# Data Format
# The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

# You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.
# Sample Execution

# $ python3 solution.py
# Enter - http://py4e-data.dr-chuck.net/comments_42.html
# Count 50
# Sum 2...

# My code was not running for some reason even though I installed BeautifulSoup with pip. So I downloaded and unzipped it within the directory of my assignemnt.

import re
import urllib
from bs4 import BeautifulSoup


target = 'http://py4e-data.dr-chuck.net/comments_301268.html'

joe = BeautifulSoup(urllib.request.urlopen(target).read(), 'html.parser')
scapped = sum(int(td.text) for td in joe.select('td:last-child')[1:])

print(scapped)
