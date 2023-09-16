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
    # Initialize a list to keep track of visited boxes
    visited = [False] * len(boxes)
    
    # Start with the first box (box 0) which is already unlocked
    visited[0] = True
    
    # Create a queue to perform BFS
    queue = [0]
    
    # Perform BFS
    while queue:
        current_box = queue.pop(0)
        
        # Check the keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to an unvisited box, mark it as visited
            if not visited[key]:
                visited[key] = True
                queue.append(key)
    
    # If all boxes have been visited, return True
    return all(visited)
