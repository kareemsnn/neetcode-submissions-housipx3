class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)}
        inDegrees = {i: 0 for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegrees[course] += 1

        
        queue = deque()
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)

        visitedNodes = 0
        while queue:
            node = queue.popleft()
            visitedNodes += 1
            for neighbors in graph[node]:
                inDegrees[neighbors] -= 1
                if inDegrees[neighbors] == 0:
                    queue.append(neighbors)

        return visitedNodes == numCourses

        