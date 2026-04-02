from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        '''
        keep the same dfs approach, if one returns true, append to res

        #INIT
        premap = {course: [prereqs]}
        visited = set()
        

        def dfs(course):
            if course in visited:
                CYCLE DETECTED
                RETURN FALSE
            add to visited

            dfs through each prereqs
            once done, discard course from visited


        res = []
        for i in range(numCourses):
            if dfs(i):
                res.append(i)


        0->2->1->0
        '''

        #INITIALIZE PREPREQS IN MAP
        premap = defaultdict(list)
        visited = set()
        seen = set()

        for course, prereq in prerequisites:
            premap[course].append(prereq)

        def dfs(course):
            #BASE CASE
            if course in seen:
                return True
            if course in visited:
                return False
            
            #BASE CASE 2, IF NO PREREQS, WE REACHED THE FINAL CLASS TO APPEND TO LIST
            if course not in premap:
                seen.add(course)
                result.append(course)
                return True

            #OTHERWISE, ADD TO VISITED
            visited.add(course)

            #TRAVERSE PREREQS FOR CYCLE DETECTION
            for prereq in premap[course]:
                if not dfs(prereq):
                    return False
            
            #REMOVE FROM VISITED
            visited.discard(course)
            seen.add(course)
            result.append(course)
            return True


        result = []
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result