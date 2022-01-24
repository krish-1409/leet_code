"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        dic = {node:Node(node.val)}
        queue = [node]
        
        while queue:
            curr = queue.pop(0)
            for i in curr.neighbors:
                if i not in dic:
                    dic[i] = Node(i.val)
                    queue.append(i)
                dic[curr].neighbors.append(dic[i])
        return dic[node]