#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def can_unlock_all(all_boxes):
    """
    Determine if all boxes can be opened.
    
    Args:
    all_boxes: List of lists, where each sublist contains keys to other boxes.
    
    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not all_boxes:
        return False

    my_keys = [0]
    keys_to_check = my_keys.copy()  # Create a copy of the initial keys

    while keys_to_check:
        new_keys = []
        for key in keys_to_check:
            for box_key in all_boxes[key]:
                if box_key not in my_keys and box_key < len(all_boxes):
                    my_keys.append(box_key)
                    new_keys.append(box_key)
        keys_to_check = new_keys
    return len(my_keys) == len(all_boxes)

# Example usage
boxes_example1 = [[1], [2], [3], []]
print(can_unlock_all(boxes_example1))  # Output: True

boxes_example2 = [[1, 4], [2], [3], [], []]
print(can_unlock_all(boxes_example2))  # Output: False
