#!/usr/local/bin/python3.5

import os
import LineCode

def exegete(words, codeNumber):
    #TODO: check is line brocken.
    #TODO: check is line multicommand.
    if(codeNumber == 1):
        return words[1]
    elif(LineCode.isDefining(words)):
        return LineCode.objectName(words)
    else:
        return 'undermake ;)'

def makeFile(filename, srcpath, despath):
    #TODO: check paths be valid.
    #TODO: implement exeptions.
    despath += "struct.txt"
    srcpath += filename
    with open(srcpath) as src, open(despath, 'w') as des:
        line = src.readline()
        words = line.split()
        codeNumber = LineCode.lineCode(words)
        if(len(words) > 0):
            des.writelines(exegete(line, codeNumber))

filename = input("\nEnter your filename: ")
srcpath = input("Enter your source file path blow:\
        \n(e.g. /Users/Hoseyn/Documents/srt.txt)\n")
despath = input("Enter your destination file blow:\
        \n(e.g. /Users/Hoseyn/Documents/srt.txt)\n")

# TODO: determine dependencies.

makeFile(filename, srcpath, despath)

# os.system('open' + despath + struct.txt)

