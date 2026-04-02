class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        English:
        starting at the first number, try all the combinations of the different numbers you can add
        [1], [1,2], [1,2,3], [2], [2,3]

        '''

        def backtrack(index, subset):

            result.append(subset[:])

            for i in range(index, len(nums)):

                #explore path, then backtrack
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        
        result = []
        backtrack(0, [])
        return result
