import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\antho\\Documents\\TestingDir'):
    print('current folder is ' + folderName)

    for subfolder in subfolders:
        print('Subfolder of ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('File Inside ' + folderName + ': ' + filename)

    print('')