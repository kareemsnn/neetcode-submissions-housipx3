class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        '''
        if current and sum(current) == target:
            append to result
            return
        
        index = 0


        for i in range(index, len(nums)):

            current.append()
            backtrack
            pop
        '''

        nums.sort()
        def backtrack(index, current, total):
            if total == target:
                result.append(current[:])
            
            # if sum(current) > target:
            #     return
            
            for i in range(index, len(nums)):
                if nums[i] + total > target:
                    return
                current.append(nums[i])
                backtrack(i, current, total + nums[i])
                current.pop()

        result = []
        backtrack(0, [], 0)
        return result