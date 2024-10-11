#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    '''Given that the first box is open, and every key
    opens the door whose number it bears, this checks
    if all the boxes can be opened by the keys found.
    '''
    opened = [False] * len(boxes)
    opened[0] = True
    keys = boxes[0]

    for key in keys:
        if 0 <= key < len(boxes) and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])

    return all(opened)
