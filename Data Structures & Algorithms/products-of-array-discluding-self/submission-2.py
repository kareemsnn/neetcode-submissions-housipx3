class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []

        for i in range(1, len(nums) + 1):
            temp = nums[:i-1]
            temp.extend(nums[i:])
            
            res.append(math.prod(temp))

        return res
            