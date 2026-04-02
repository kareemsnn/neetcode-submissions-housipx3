class Solution:
    def isValid(self, s: str) -> bool:
        openP = {'(', '[', '{'}
        matching = {')':'(', '}':'{',']':'['}

        stack = []

        for p in s:
            if p in openP:
                stack.append(p)
            elif stack and matching[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []