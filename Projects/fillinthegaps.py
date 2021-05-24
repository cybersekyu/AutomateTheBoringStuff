#! python3
# fillinthegaps.py - find all files with a given prefix in a folder and locate any numbering gap and rename the succeeding files. 


import os, shutil

#Run through all the files and check for gaps in numbering.

GapFolder = os.path.abspath('C:\\Users\\antho\\Documents\\TestingDir\\test6')

for foldername, subfolder, filename in os.walk(GapFolder):
    number = 1
    for filenames in filename:
        gapfilename = "spam00" + str(number) + ".txt"
        if filenames != gapfilename:
            print("Renaming... " + filenames + " to " + gapfilename)
            shutil.move(GapFolder + '\\' + filenames, GapFolder + '\\' + gapfilename) #Rename succeeding files to close the gap.
        number = number + 1


#TODO: Bonus create a file that can insert gaps so that a new file can be added.