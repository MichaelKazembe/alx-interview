#!/usr/bin/python3
"""
0. Lockboxes
mandatory
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    # Create a set to keep track of the keys we have
    keys = {0}
    # Iterate through the lockboxes
    for i, box in enumerate(boxes):
        # Check if we have the key to open the current lockbox
        if i in keys or any(key in keys for key in box):
            # Add the keys from the current lockbox to our set
            keys.update(box)
        else:
            # If we don't have the key to open the current lockbox
            return False

    # If we successfully opened all lockboxes, return True
    return True
