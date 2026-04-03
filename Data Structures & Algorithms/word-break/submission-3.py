class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s[i : i + len(word)] == word:
                    print(s[i : i + len(word)])
                    dp[i] = dp[i + len(word)] or dp[i]
            
        return dp[0]
