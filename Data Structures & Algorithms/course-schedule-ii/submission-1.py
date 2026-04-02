class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegrees = {i : 0 for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        num, result = 0, []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            num += 1
            for neighbor in graph[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        if num == numCourses:
            return result
        else:
            return []
