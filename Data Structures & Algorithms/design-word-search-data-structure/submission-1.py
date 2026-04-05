class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.end = True

    def search(self, word: str) -> bool:
        '''
        if '.':
            for each key, child in curr.children:
                if not dfs(child, i + 1):
                    return False

        else:
            if word[i] not in curr.children return false, 
            else curr = curr.children[char]
            return bool == end
        '''
        
        def dfs(curr, index):

            for i in range(index, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]

            return curr.end

        curr = self.root
        return dfs(curr,0)