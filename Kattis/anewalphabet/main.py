#!/usr/bin/env python3
import string
import sys
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
new_alphabet_list = ['@','8','(','|)','3','#','6','[-]','|','_|','|<','1','[]\/[]','[]\[]','0','|D','(,)','|Z','$',"']['",'|_|','\/','\/\/','}{','`/','2']
def seperate(strInput):
    strInput = strInput.lower()
    newString = ''
    for x in strInput:
        if x >= 'a' and x <= 'z':
            temp = conversion(x)
            newString = newString + temp
        else:
            newString = newString + x
    return newString

def conversion(charInput):
    for i in range(26):
        if charInput == alphabet_list[i]:
            return new_alphabet_list[i]
def main():
    data=sys.stdin.readline()
    print(seperate(data))

if __name__  == "__main__":
    main()