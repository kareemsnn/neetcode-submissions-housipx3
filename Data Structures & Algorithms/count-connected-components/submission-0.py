class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        visited = set()
        count = 0

        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)

        def dfs(node, parent):
            if node in visited:
                return 0

            visited.add(node)
            
            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
            return 1
        

        for i in range(n):
            count += dfs(i, -1)

        return count