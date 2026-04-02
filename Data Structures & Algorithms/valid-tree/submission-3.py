from collections import defaultdict
class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        look at the edges, if i see a destination node can be reached from more than 1 node, return False

        build an adjacency list {node : [children]}
        {key, []}

        for node in range(n):
            dfs through node and keep track of visited nodes.
            If node is visited, return False
        
        return True
        '''

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for child in adjList[node]:
                if child == parent: 
                    continue
                if not dfs(child, node):
                    return False
            return True


        visited = set()
        adjList = defaultdict(list)

        for parent, child in edges:
            adjList[parent].append(child)
            adjList[child].append(parent)

        return dfs(0, -1) and len(visited) == n
