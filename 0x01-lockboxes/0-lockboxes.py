#!/usr/bin/python3
"""Solves the lock boxes puzzle"""

from typing import List, Dict, Optional

def look_next_opened_box(opened_boxes: Dict[int, Dict[str, List[int]]]) -> Optional[List[int]]:
    """Looks for the next opened box
    Args:
        opened_boxes (Dict[int, Dict[str, List[int]]]): Dictionary which contains boxes already opened
    Returns:
        Optional[List[int]]: List with the keys contained in the opened box, or None if no more boxes to check
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """Check if all boxes can be opened
    Args:
        boxes (List[List[int]]): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    aux = {0: {'status': 'opened', 'keys': boxes[0]}}
    
    while True:
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                if key >= len(boxes):
                    continue
                if aux.get(key) and aux.get(key).get('status') == 'opened/checked':
                    continue
                aux[key] = {'status': 'opened', 'keys': boxes[key]}
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)

def main():
    """Entry point"""
    print(canUnlockAll([[]]))  # Example call

if __name__ == '__main__':
    main()
