class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        prereqs = [course, prereq]
        for each [course, prereq], keep track in preMap[course] = [prerequisite]
        go thru each pair and dfs. we need to make sure that no cycles are found
        keep track of seen courses using a visited set

        pseudocode:
        preMap = {}
        visited = set()

        for i in range(numCourses):
            initialize preMap[i] = []

        for course, prereq in prerequisites:
            premap[course] = prereq

        def dfs(course):
            - if preMap[course] in visited: return False
            - for prereq in preMap[course]: 
            - if prereq dfs():
            - return true


        dfs(0):

        for prereqs in preMap[course]:
            1
        '''

        preMap = {}
        visited = set()

        for i in range(numCourses):
            preMap[i] = []

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        def dfs(course):
            if course in visited:
                return False

            if preMap[course] == []:
                return True

            visited.add(course)

            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
                    
            visited.discard(course)
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                print(c)
                return False
        return True
