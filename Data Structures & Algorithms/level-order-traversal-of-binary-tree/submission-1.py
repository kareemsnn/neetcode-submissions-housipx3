# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        '''
        initialize q with root
        while q:
            row = []
        for nodes in q:
            q.append(node.right)
            q.append(node.left)
            row.append(node)

        result.append(row)
        '''
        q = deque([root])

        while q:
            row = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    row.append(node.val)
            if row:
                result.append(row)

        return result