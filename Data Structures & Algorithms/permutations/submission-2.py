class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(index):

            if index == len(nums):
                return [[]]

            perms = dfs(index + 1)
            curr = nums[index]
            output = []

            for p in perms:
                for i in range(len(p) + 1):
                    output.append(p[:i] + [curr] + p[i:])
            
            return output
        
        return dfs(0)