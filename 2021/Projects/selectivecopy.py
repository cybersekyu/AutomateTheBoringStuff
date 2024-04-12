#! python3
# selectivecopy.py - copy files base on defined extension .jpg or .pdf to a new location

import shutil, os

#walks through a folder tree and look for define extension
ThisFolder = os.path.abspath('.')
ThatFolder = os.path.abspath('C:\\Users\\antho\\Documents\\TestingDir')

for foldername, subfolders, filenames in os.walk(ThisFolder):
    for filename in filenames:
        if filename.endswith(('.jpg','.pdf')):
            fileto = foldername + '\\' + filename
            print('Moving... ' + fileto + ' to ' +  ThatFolder)
           
# move the files to a specified new location
            shutil.move(fileto, ThatFolder)

print('Finished.')