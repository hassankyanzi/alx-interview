#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""

def can_unlock_all(boxes):
    """
    Function that checks if all boxes can be unlocked.
    Uses a stack for a depth-first search (DFS) approach to track and unlock boxes.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)

# Example usage
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(can_unlock_all(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(can_unlock_all(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(can_unlock_all(boxes))  # False
