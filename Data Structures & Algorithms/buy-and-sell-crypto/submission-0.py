class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxDiff = 0
        l = 0
        r = 1

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            elif (prices[r]-prices[l]) > maxDiff:
                maxDiff = prices[r] - prices[l]
        return maxDiff
            
            
