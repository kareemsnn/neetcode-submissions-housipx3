class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            middle = (l + r) // 2
            
            if nums[r] > nums[middle]:
                r = middle
            else:
                l = middle + 1
        
        return nums[l]



#[6,1,2,3,4,5]