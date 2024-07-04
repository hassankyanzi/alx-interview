# Lockboxes

## Project Description

This project involves solving the "Lockboxes" problem, where you need to determine if all boxes can be unlocked given an initial set of keys in the first box. The solution requires implementing a method that efficiently determines the unlockability of all boxes using Python.

## Concepts Used

- **Lists and List Manipulation**: Accessing, iterating, and modifying lists.
- **Graph Theory Basics**: Understanding traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS).
- **Algorithmic Complexity**: Analyzing the time and space complexity of the solution.
- **Recursion**: Utilizing recursive approaches to traverse through the boxes and keys.
- **Queue and Stack**: Using queues and stacks for BFS or DFS.
- **Set Operations**: Keeping track of visited boxes and available keys.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder is mandatory
- Code should be documented
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Task

### 0. Lockboxes

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to other boxes.

Write a method that determines if all the boxes can be opened.

- **Prototype**: `def canUnlockAll(boxes):`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

### Example Usage

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
