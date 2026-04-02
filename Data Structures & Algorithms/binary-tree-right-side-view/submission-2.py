# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        cycle thru each node
        set each node to be "rightNode"
        ultimately when the loop is done, the last one will acc be the right jawn
        apppend that
        '''

        res = []
        q = deque([root])

        while q:
            rightNode = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)
                
            if rightNode:
                res.append(rightNode.val)
        return res