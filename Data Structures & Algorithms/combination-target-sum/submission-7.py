class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            9
        
        we're gonna start with dfs(target):
        if we're < 0: return

        if target == 0, append path to result and return
        else

        for num in nums:
            if target - nums >= 0:
                path.append
                dfs()
            
        '''

        res = []

        def dfs(target, i, path):
            if target == 0:
                res.append(path[:])
                return
            print(target)
            for j in range(i,len(nums)):
                if target - nums[j] >= 0:
                    path.append(nums[j])
                    dfs(target - nums[j], j, path)
                    path.pop()

        dfs(target, 0, [])
        return res