#! python3
# madlibs.py - reads a text files and look for word ADJECTIVES,NOUN,ADVERB or VERB and prompts users to replace it

import re

#Read a text file.

madlibsfile = open('madlibs.txt')
content = madlibsfile.read()

textcontent = re.split(r'\W+', content)
#Look for word ADJECTIVES,NOUN,ADVERB or VERB. Prompt user to replace occurences.
output = content

for i in textcontent:
    if i == 'ADJECTIVE':
        textRegex = re.compile(r'(ADJECTIVE)')
        print("Enter an ADJECTIVE:")
        adj = input()
        output = textRegex.sub(adj,output,1)
    elif i == 'NOUN':
        textRegex = re.compile(r'(NOUN)')
        print("Enter a NOUN:")
        noun = input()
        output = textRegex.sub(noun,output,1)
    elif i == 'ADVERB':
        textRegex = re.compile(r'(ADVERB)')
        print("Enter an ADVERB:")
        adv = input()
        output = textRegex.sub(adv,output,1)
    elif i == 'VERB':
        textRegex = re.compile(r'(VERB)')
        print("Enter a VERB:")
        verb = input()
        output = textRegex.sub(verb,output,1)


#print the result in the screen and save to new text file.
newmadlibfile = open('newMadlib.txt', 'w')
newmadlibfile.write(output)
newmadlibfile.close
print(output)