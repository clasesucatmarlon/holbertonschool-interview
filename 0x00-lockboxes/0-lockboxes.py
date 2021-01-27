#!/usr/bin/python3

def canUnlockAll(boxes):
    newlist = []
    total = len(boxes)

    for array in boxes:
        if (len(array) == 0 and array is not boxes[total - 1]):
            return False
        for j in array:
            newlist.append(j)


    for i, k in enumerate(boxes):
        if i in newlist or i < (total - 1):
            return True
        else:
            return False
