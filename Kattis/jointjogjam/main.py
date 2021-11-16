#! /usr/bin/env python3
## 1) disrance (x1: int, y1: int, x2: int, y2: int) -> returns a float
## 2) finding the max value of the 2
##    i.    def answer(Distance1 :float, Distance2: float) -> float
### A. Always right the tests first then the code because the code is always the harder part
###
#   x2 - x1
#
#
import math
def distance(x1:int,y1:int,x2:int,y2:int) -> float:
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
#return the max of d0 and d1    
def answer(d0:float,d1:float) -> float:
    return max(d0, d1)

def main():
    data=[int(x)for x in input().split(' ')]
    assert(len(data) == 8)
    d0 = distance(data[0], data[1],data[2], data[3])
    d1 = distance(data[4],data[5],data[6], data[7])
    print(answer(d0,d1))

if __name__  == "__main__":
    main()