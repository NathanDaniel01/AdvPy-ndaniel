#!/usr/bin/env python3
import math
import sys
answers= []
def getsqr(number):
    ans = number * number
    return ans

def check(ans, hypotenus):
    sqrts = math.sqrt(ans)
    if sqrts == int(hypotenus):
        answers.append("right")
        return ("right")
    else:
        answers.append("wrong")
        return ("wrong")
def main():
    a = []
    a = sys.stdin.readline().split(' ')
    hypotnuse  = max(int(a[0]), int(a[1]), int(a[2])) 
    while(int(a[0]) != 0 and int(a[1]) != 0 and int(a[2]) != 0  ):
        if int(a[0]) ==  hypotnuse:
            firstSquare = getsqr(int(a[2]))
            seccondSquare = getsqr(int(a[1]))
            ans = firstSquare + seccondSquare
            check(ans, int(hypotnuse))
        elif int(a[1]) ==  hypotnuse:
            firstSquare = getsqr(int(a[0]))
            seccondSquare = getsqr(int(a[2]))
            ans = firstSquare + seccondSquare
            check(ans, int(hypotnuse))
        else:
            firstSquare = getsqr(int(a[0]))
            seccondSquare = getsqr(int(a[1]))
            ans = firstSquare + seccondSquare
            check(ans, int(hypotnuse))
        a = sys.stdin.readline().split(' ')
        hypotnuse  = max(int(a[0]), int(a[1]), int(a[2])) 

    for i in answers:
        print (i)
    return None
if __name__  == "__main__":
    main()