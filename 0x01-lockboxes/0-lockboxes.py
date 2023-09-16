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
    keys = {0: True}
    n_boxes = len(boxes)

    while True:
        n_keys = len(keys)

        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n_boxes:
                        keys[j] = True
                boxes[i] = None

        if len(keys) <= n_keys:
            break

    return len(keys) == n_boxes
