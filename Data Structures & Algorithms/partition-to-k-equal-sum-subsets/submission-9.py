class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        

        if sum(nums) % k != 0:
            return False
        
        used = [False] * len(nums)
        target = sum(nums) // k
        nums.sort(reverse=True)



        def backtrack(index, currSum, buckets):
            if buckets == 0:
                return True

            if currSum == target:
                return backtrack(0, 0, buckets - 1)

            for i in range(index, len(nums)):
                if used[i] or nums[i] + currSum > target:
                    continue
                
                used[i] = True
                if backtrack(i+1, currSum + nums[i], buckets):
                    return True
                used[i] = False
            return False

        return backtrack(0, 0, k)
                        

            
            #IF PROCESSED
