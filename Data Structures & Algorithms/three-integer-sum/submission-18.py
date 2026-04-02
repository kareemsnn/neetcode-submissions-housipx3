class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-1):
            l,r = i + 1, len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    if [nums[i],nums[l],nums[r]] not in result:
                        result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1

            
        return result


