class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):  # Recursive DFS
                        return True
                elif neighbor != parent:  # Back edge detected
                    return True
            return False

        # Step 1: Build the graph as an adjacency list
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

            # Step 2: Detect cycle by performing DFS
            visited = {key: False for key in graph.keys()}
            if dfs(u, -1):  # Start DFS from one of the nodes
                return [u, v]  # Return the edge causing the cycle



