# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        res = 0
        dfs(node, path):
            if not node:
                return

            if node.val > max(path):
                res += 1
            
            path.append(node.val)
            dfs(node.left, path)
            dfs(node.right, path)
            path.remove(node.val)


        dfs(root, [-1])
        '''


        res = 0
        def dfs(node, maxNum):
            nonlocal res
            if not node:
                return

            if node.val >= maxNum:
                res += 1

            num = max(maxNum, node.val)
            dfs(node.left, num)
            dfs(node.right, num)


        dfs(root, float('-inf'))
        return res