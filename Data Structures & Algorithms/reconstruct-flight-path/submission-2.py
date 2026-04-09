import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adjList = defaultdict(list)
        tickets.sort()
        for start, end in tickets:
            adjList[start].append(end)
        
        res = ["JFK"]

        def dfs(start):
            if len(res) == len(tickets) + 1:
                return True
            
            if start not in adjList:
                return False

            temp = adjList[start][:]
            for i, node in enumerate(temp):
                res.append(node)
                adjList[start].pop(i)

                if dfs(node):
                    return True
                
                res.pop()
                adjList[start].insert(i, node)
            return False
        

        dfs("JFK")
        return res