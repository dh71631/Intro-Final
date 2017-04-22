# Donald Hartwick
# COP 2271C
# Final Exam
# This code stores a local txt file name and a url for a remote txt file as a list.

import string
from urllib.request import urlretrieve

def main():
    userInput = str(input("Please Enter L For Local File W for Web File or Q for Quit: "))
    if(userInput.upper() == 'L'):
        getLocalFile()
    elif(userInput.upper() == 'W'):
        getWebFile()
    elif(userInput.upper() == 'Q'):
        print("Goodbye")
    else:
        main()
def getWebFile():
    urlretrieve('http://tholianwebdesign.com/special/babynames.txt', 'webbabynames.txt')
    try:
        inputFile = open('webbabynames.txt', 'r')
    except:
        print("Problem With Web Input Please Make Another Selection")
        main()
    parseFile(inputFile)
def getLocalFile():
    userInput = str(input("Plese Enter The Local File Path: "))
    try:
        inputFile = open(userInput, 'r')
    except:
        getLocalFile()
    parseFile(inputFile)
def parseFile(inputFile):
    contents = inputFile.read()
    contents = contents.replace(',', '')
    contents = contents.split()
    for x in range(0, len(contents)):
        try:
            contents[x] = int(contents[x])
        except:
            pass
    boys = []
    girls = []
    both = []
    for x in range(0, len(contents)):
        if(isinstance(contents[x], str)):
            choice = str(input("Is " + contents[x] + " A Boy Name, Girl Name, or Both? (b, g, y default): "))
            if(choice.lower() == 'b'):
                boys.append(contents[x])
            elif(choice.lower() == 'g'):
                girls.append(contents[x])
            else:
                both.append(contents[x])
    boysNames = ''
    for x in range(0, len(boys)):
        boysNames += "\n" + boys[x]
    girlsNames = ''
    for x in range(0, len(girls)):
        girlsNames += "\n" + girls[x]
    bothNames = ''
    for x in range(0, len(both)):
        bothNames += "\n" + both[x]
    inputFile.close()
    outFile = open('boysnames.txt', 'w')
    outFile.write(boysNames)
    outFile.close()
    outFile = open('girlsnames.txt', 'w')
    outFile.write(girlsNames)
    outFile.close()
    outFile = open('bothnames.txt', 'w')
    outFile.write(bothNames)
    outFile.close()

main()

