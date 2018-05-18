#!/usr/local/python3.5

def macros(words):
    if(words[0][1:] == 'define'):
        return 1
    return 0

def block(words):
    if(words[0][0] == '{'):
        return 11
    return 12

def clearName(word):
    result = 'fu'
    end = word.find('(')
    if(end == -1):
        result = 'fi'
        end = word.find(';')
    return result + word[:end]

def objectName(words):
    if(words[0] in ['void', 'static', 'int', 'bool',\
            'double', 'float', 'virtual']):
        return words[1:]
    else:
        return clearName(words[0])

def isDefining(words):
    if(words[0] in ['void', 'static', 'int', 'bool',\
            'double', 'float', 'virtual']):
        return True
    return False

def defineCode(words):
    if(words[0] == 'void'):
        return 21 + defineCode(words)
    elif(words[0] == 'int'):
        return 22 + defineCode(words)
    elif(words[0] == 'bool'):
        return 23 + defineCode(words)
    elif(words[0] == 'double'):
        return 24 + defineCode(words)
    elif(words[0] == 'float'):
        return 25 + defineCode(words)
    elif(words[0] == 'static'):
        return 100 + defineCode(words)
    elif(words[0] == 'virtual'):
        return 200 + defineCode(words)
    else:
        return 0

def lineCode(words):
    if(words[0][0] == '#'):
        return macros(words)
    elif(line[0] in ['{','}']): #TODO: Add line resume checking.
        return block(words)
    elif(isDefining(words)):
        return defineCode(words)
