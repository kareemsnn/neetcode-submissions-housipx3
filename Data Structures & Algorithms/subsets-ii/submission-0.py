class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        English:
            for each number, look at all the possible
            backtrack(0)

            0, 1, 2, 3

        '''

        def backtrack(index, current):
            
            result.append(current[:])

            for i in range(index, len(nums)):

                if i > index and nums[i-1] == nums[i]:
                    continue

                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()




        result = []
        nums.sort()
        backtrack(0, [])
        return result