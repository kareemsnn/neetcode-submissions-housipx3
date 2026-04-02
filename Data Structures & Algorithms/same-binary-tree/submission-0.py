# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        '''
        bfs starting from top:
        add both p and q into queue.
        pop from queue twice. if both are equal, append their .left and .right together
        '''

        q = deque([p,q])

        while q:
            a = q.popleft()
            b = q.popleft()

            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            q.append(a.left)
            q.append(b.left)
            q.append(a.right)
            q.append(b.right)
        return True
        
