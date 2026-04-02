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


        def backtrack(index, current):
            print(sum(current))
            if sum(current) == target:
                result.append(current[:])

            if sum(current) > target:
                return
            
            for i in range(index, len(nums)):
                current.append(nums[i])
                print(current)
                backtrack(i, current)
                current.pop()

        result = []
        backtrack(0, [])
        return result