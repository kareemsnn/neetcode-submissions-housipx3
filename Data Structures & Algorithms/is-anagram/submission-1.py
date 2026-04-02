class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = Counter(s)

        for char in t:
            if char in freq and freq[char] > 0:
                freq[char] -= 1
            else:
                return False
        return True
