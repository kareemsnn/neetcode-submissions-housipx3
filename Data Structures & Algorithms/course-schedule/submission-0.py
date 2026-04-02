class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}
        visited = set()

        for i in range(numCourses):
            adjList[i] = []
        for pre, course in prerequisites:
            adjList[course].append(pre)
    
        def dfs(course):
            if course in visited:
                return False

            if adjList[course] == []:
                return True

            visited.add(course)
            for pre in adjList[course]:
                flag = dfs(pre)
                
            return flag

        for pre, course in prerequisites:
            flag = dfs(pre)
            if not flag:
                return False
        return True


    #once i get a [0,1], check adjList[1] and see 0
    # call 0 to dfs and check its adjList. if visited, return False

    #dfs(1)
    #dfs(0)
    # 
    # 
    # 
    #     