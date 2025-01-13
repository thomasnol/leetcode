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
        if not node:
            return None
        
        stk = [node]
        oton = {}
        visited = set()
        visited.add(node)

        while stk:
            cur = stk.pop()
            oton[cur] = Node(val=cur.val)
            for nei in cur.neighbors:
                if nei in visited: continue
                visited.add(nei)
                stk.append(nei)
        
        for key, val in oton.items():
            for nei in key.neighbors:
                val.neighbors.append(oton[nei])
        
        return oton[node]