class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        build adj list
        prereqs[a].append(b)

        res = []
        for i in range n:
            if not dfs(i):
                return []
        return res

        dfs(course):

            if in seen:
                return False
            
            for each nei:
                seen.add
                if not dfs(nei):
                    return False
                seen.discard
            res.append(course)        
        '''

        prereqs = collections.defaultdict(list)
        for course, pre in prerequisites:
            prereqs[course].append(pre)
        seen = set()
        visited = set()
        res = []

        def dfs(course):
            
            if course in seen:
                return False
            if course in visited:
                return True
            
            seen.add(course)
            for nei in prereqs[course]:
                print(nei)
                if not dfs(nei):
                    return False
            seen.discard(course)
            res.append(course)
            visited.add(course)
            return True
        
        
        for i in range(numCourses):
            dfs(i)
        return res if len(res) == numCourses else []

