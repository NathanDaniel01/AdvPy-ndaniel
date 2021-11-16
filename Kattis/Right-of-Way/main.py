#!/usr/bin/env python3
compass = ["North", "West", "South", "East"]
def main():
    data =input()
    datalist = data.split()
    print(rightofway(datalist))
def rightorentation(start):
    for i in range(4):
        if start == compass[i]:
            if i == 3:
                right = compass[0]
            else:
                right = compass[i + 1]
            return right
    return "Error"
def straightorentation(start):
    for i in range(4):
        if start == compass[i]:
            if i > 1:
               straight = compass[i%2]
            else:
                straight = compass[i + 2]
            return straight
    return "Error"
def leftorentation(start):
    for i in range(4):
        if start == compass[i]:
            if i == 0:
               straight = compass[3]
            else:
                straight = compass[i - 1]
            return straight
    return "Error"
def rightofway(datalist):
    right = rightorentation(datalist[0])
    straight = straightorentation(datalist[0])
    left = leftorentation(datalist[0])
    end = datalist[1]
    opposite = datalist[2]
    if end == straight and opposite == right:
        return "Yes"
    elif end == left and opposite == right:
        return "Yes"
    elif end == left and opposite == straight:
        return "Yes"
    else:
        return "No"
if __name__  == "__main__":
    main()