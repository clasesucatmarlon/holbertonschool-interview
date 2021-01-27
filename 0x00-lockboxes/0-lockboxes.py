#!/usr/bin/python3

def canUnlockAll(boxes):
    """ Write a method that determines if all the boxes can be opened
    """
    pocket = [0]
    for key in pocket:
        for key_box in boxes[key]:
            if key_box not in pocket:
                if key_box < len(boxes):
                    pocket.append(key_box)
    if len(pocket) == len(boxes):
        return True
    return False
