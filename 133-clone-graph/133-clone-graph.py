"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldhash = {}
        
        def dfs(node):
            if node in oldhash:
                return oldhash[node]
            newnode = Node(node.val)
            oldhash[node] = newnode
            for nei in node.neighbors:
                newnode.neighbors.append(dfs(nei))
            return newnode
        return dfs(node) if node else None
            
        