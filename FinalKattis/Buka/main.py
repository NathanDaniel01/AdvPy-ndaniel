#!/usr/bin/env python3
import string
import sys

def multiply(firstnumber, seccondnumber):
    ans =  int(firstnumber)* int(seccondnumber)
    return ans
def add(firstnumber, seccondnumber):
    ans =  int(firstnumber) + int(seccondnumber)
    return ans

def main():
   
    firstnumber=sys.stdin.readline().strip('\n')
    operaton=sys.stdin.readline().strip('\n')
    seccondnumber=sys.stdin.readline().strip('\n')
    if operaton == "*":
      print( multiply(firstnumber, seccondnumber))
    else:
       print(add(firstnumber, seccondnumber))



if __name__  == "__main__":
    main()