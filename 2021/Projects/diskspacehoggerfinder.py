#! python3
# diskspacehoggerfinder.py - finds files and folders that take up huge disk space and delete it base on the specified size.

import os, shutil

#walk through the folder and find the size of files and folders.
HogFolder = os.path.abspath('C:\\Users\\antho\\Downloads')

#print the size and delete the files
for foldername, subfolder, filename in os.walk(HogFolder):
    for filenames in filename:
        filesize = os.path.getsize(foldername + '\\' + filenames)
        if filesize >= 100000000:
            print('Deleting... ' + str(filesize) + '... ' + foldername + '\\' + filenames)
            #os.unlink(foldername + '\\' + filenames)