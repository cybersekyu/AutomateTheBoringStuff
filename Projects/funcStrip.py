import re

def funcStrip(stripstr, stripr=None):
    if stripr == None:
        #print("remove whitespace")
        StripRegex = re.compile(r'[\S].*[\S]')
    else:
        #print("will remove pattern")
        StripRegex = re.compile(r'[^' + stripr + r'].*[^' + stripr + r']')
    
    mo = StripRegex.search(stripstr)
    print(mo.group())
        

funcStrip("ASAASAASAASAhave you worked outASA", "ASA")
funcStrip("    have you worked out     ")