#!/usr/bin/python3
# dirtily depend on shell command 'sleep' and 'clear'

from os import system,linesep
from time import ctime

ls=linesep

'''
ctt=content to print. No default.
opt={
end: the string to print after printing the argument ctt
width: the width of screen, measured in 'num of chars to fulfill a row'
}. {end:'\n', width:180} as default.

'''
def printCLImiddle(ctt,**opt):
    try:
        theend=opt['end']
    except KeyError as ke:
        theend='\n'

    try:
        width=opt['width']
    except KeyError as ke:
        width=180

    print(' '*(int(width/2)-1-int(len(ctt)/2))+ctt,end=theend)


while True:
    system('clear')
    print(linesep*23)
    prompt='Press Ctrl-z to exit'
    printCLImiddle(ctime())
    print(linesep*1)
    printCLImiddle(prompt)
#    print(linesep*33)

    system('sleep 1')
    
