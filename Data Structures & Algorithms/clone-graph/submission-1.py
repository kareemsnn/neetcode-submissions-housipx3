"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        {1 : 1'}

        if not node return none
        we want to traverse the original graph. 
        with each node, create a new node.
        check node's neighbors. if neighbor's have copies, link the copies
        else, dfs.
        if node not in oldToNew, append it with newNode
        '''

        if not node:
            return None

        oldToNew = {}

        # def dfs(node):
        #     print(node.val)
        #     if node in oldToNew:
        #         return oldToNew[node]    
        #     oldToNew[node] = Node(node.val)
        #     newNode = oldToNew[node]

        #     for nei in node.neighbors:
        #         if nei in oldToNew:
        #             # newNeighbor = oldToNew[nei]
        #             newNode.neighbors.append(dfs(nei))
        #         else:
        #             oldToNew[nei] = Node(nei.val)
        #             newNeighbor = oldToNew[nei]
        #             newNode.neighbors.append(newNeighbor)

        def dfs(node):
            print(node.val)
            if node in oldToNew:
                return oldToNew[node]    
            oldToNew[node] = Node(node.val)
            newNode = oldToNew[node]

            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            return newNode

        return dfs(node)