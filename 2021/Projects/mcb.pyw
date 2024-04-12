#! python3
#mcb.pyw - Saves and loads pieces of text to the clipboard
#Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe mcb.pyw keyword - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to clipboard.
#       py.exe mcb.pyw delete <keyword> - Deletes saved keyword.
#       py.exe mcb.pyw purge - Deletes all saved keywords.
# create a bat file in C:\<user>\ to run commands via win + R or run


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')


#Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    #delete specified keyword stored. 
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    #delete keywords, List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'purge':
        for i in list(mcbShelf.keys()):
            del mcbShelf[i]            
        
mcbShelf.close()