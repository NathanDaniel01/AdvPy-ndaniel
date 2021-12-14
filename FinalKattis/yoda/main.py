#!/usr/bin/env python3
import string
import sys
def Compare(data1, data2):
    newdata1 = []
    newdata2 = []
    if len(data1) > len(data2):
        for i in range(len(data1)):
            if i >= len(data2):
                newdata1.append(data1[i]) 
            elif  data1[i] > data2[i]:
                newdata1.append(data1[i]) 
            elif data1[i] < data2[i]:
                newdata2.append(data2[i]) 
            else:
                newdata1.append(data1[i]) 
                newdata2.append(data1[i]) 
    elif len(data1) < len(data2):
          for i in range(len(data2)):
            if i >= len(data1):
                newdata2.append(data2[i]) 
            elif  data2[i] > data1[i]:
                newdata2.append(data2[i]) 
            elif data2[i] < data1[i]:
                newdata1.append(data1[i]) 
            else:
                newdata2.append(data2[i]) 
                newdata1.append(data2[i]) 
    else:
         for i in range(len(data2)):
            if  data2[i] > data1[i]:
                newdata2.append(data2[i]) 
            elif data2[i] < data1[i]:
                newdata1.append(data1[i]) 
            else:
                newdata2.append(data2[i]) 
                newdata1.append(data2[i]) 
    
    #printnumbers(newdata1,newdata2)
    return(newdata1)

def printnumbers(newdata1,newdata2):
    printdata1 = 0
    printdata2 = 0
    for i in reversed(range(len(newdata1))):
        printdata1 = printdata1 +  newdata1[i] * pow (10, i)
    for i in reversed(range(len(newdata2))):
        printdata2 = printdata2 + newdata2[i] * pow (10, i) 
    if len(newdata1) == 0:
       # print('YODA')
        #print(printdata2)
        return "1YODA"
    elif len(newdata2) == 0:
       # print(printdata1)
       # print('YODA')
        return "2YODA"
    else: 
       #print(printdata1)
       # print(printdata2)
        return printdata1
def main():
   
    firstnumber=sys.stdin.readline().strip('\n')
    seccondnumber=sys.stdin.readline().strip('\n')
    data1 = [int(i) for i in reversed(firstnumber)]
    data2 = [int(i) for i in reversed(seccondnumber)]
    Compare(data1,data2)



if __name__  == "__main__":
    main()