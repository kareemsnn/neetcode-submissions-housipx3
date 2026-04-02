class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        my_set = set()

        maxw = 0

        l=0

        for r in range(len(s)):

            while s[r] in my_set:

                my_set.remove(s[l])
                l+=1
            
            my_set.add(s[r])

            maxw = max(maxw, r-l+1)

        return maxw



