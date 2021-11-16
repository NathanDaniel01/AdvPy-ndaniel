#!/usr/bin/env python3
def main():
    inputtotal =input()
    TotalBites = int(inputtotal)
    data =input()
    datalist = data.split()
    printout( count_mumbles(datalist, TotalBites))

def count_mumbles(datalist, TotalBites):
    count = 0
    totalcount = 0
    iscorrect = True
    for i in range(TotalBites):
            count = i + 1 
            if datalist[i] == str(count):
                totalcount += totalcount
            elif datalist[i] == "mumble":
                totalcount += totalcount
            else:
                iscorrect = False
                break
    return iscorrect
def printout(iscorrect):
    if iscorrect == False:
         print("something is fishy")
    else: 
        print("makes sense")
    
if __name__  == "__main__":
    main()