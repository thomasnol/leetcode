"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        # breadth first search
        # mapping old nodes to new nodes?
        old_to_new = {}
        queue = [node]
        old_to_new[node] = Node(node.val)

        while queue:
            oldnode = queue.pop(0)
            for neighbor in oldnode.neighbors:
                if neighbor not in old_to_new: # if not visited / not exists
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new[oldnode].neighbors.append(old_to_new[neighbor])
        return old_to_new[node]