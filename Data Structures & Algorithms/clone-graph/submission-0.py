"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        new = {}
        
        def dfs(curr):
            if curr in new:
                return new[curr]
            clone = Node(curr.val)
            new[curr]=clone

            for n in curr.neighbors:
                clone.neighbors.append(dfs(n))

            return clone
        return dfs(node)