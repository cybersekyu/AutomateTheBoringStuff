#! python3
# regexsearchfile.py - open txt files and search for user supplied regex expression

import re, os

#Open txt files 
txtfiles=os.listdir('.\\textfile')
#find the match of regex expression and output the result
for i in txtfiles:
    opentxt = open(i)
    print('Enter keyword to search:')
    keywordz = input()
    textRegex = re.compile(keywordz)
    TextMatch = textRegex.findall(opentxt.read())
    print(TextMatch)
    opentxt.close()
