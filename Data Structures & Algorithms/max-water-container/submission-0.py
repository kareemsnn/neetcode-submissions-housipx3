class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = l + 1
        result = 0

        for l in range(len(heights)):
            r = l + 1
            while r < len(heights):
                area = min(heights[l], heights[r]) * (r - l)
                print(area)
                if area > result:
                    result = area
                r += 1
        return result