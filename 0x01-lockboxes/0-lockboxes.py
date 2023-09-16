#!/usr/bin/python3
""" Lockboxes task """


def canUnlockAll(boxes):
    """
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
