import os

def getFileList(directory):
    files = os.listdir(directory)
    for i in files:
        try:
            getFileList(i)
        except FileNotFoundError:
            "Nothing here."
    print(files)

getFileList("/Users/ASUS/Documents/Python Proj")
