class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        root = self

        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        
        root.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        result = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()

        def dfs(r, c, node, path):
            #IF OUT OF BOUNDS:
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in seen:
                return
            
            if board[r][c] not in node.children:
                return
            
            node = node.children[board[r][c]]
            path += board[r][c]
            seen.add((r,c))

            if node.end and path not in result:
                result.add(path)

            for x,y in directions:
                dfs(r + x, c + y, node, path)
            
            seen.discard((r,c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root, "")
                    
        return list(result)        