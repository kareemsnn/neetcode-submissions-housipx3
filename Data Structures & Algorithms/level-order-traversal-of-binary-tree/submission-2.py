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
        bfs
        initialize q with root
        while q:
            row = []
        for nodes in q:
            q.append(node.right)
            q.append(node.left)
            row.append(node)

        result.append(row)

        '''
        # q = deque([root])

        # while q:
        #     row = []
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node:
        #             q.append(node.left)
        #             q.append(node.right)
        #             row.append(node.val)
        #     if row:
        #         result.append(row)

        # return result

        '''
        dfs
        '''

        res = []

        def dfs(node, depth):
            if not node:
                return
            
            if depth == len(res):
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 0)
        return res

