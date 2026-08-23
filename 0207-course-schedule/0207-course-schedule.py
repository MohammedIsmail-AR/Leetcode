class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
            
        # 2. Collect all courses that have 0 prerequisites
        queue = [i for i in range(numCourses) if indegree[i] == 0]
        
        # 3. Process the courses one by one
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            
            # Remove this course as a requirement for neighbor courses
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. If we successfully processed all courses, no cycle exists!
        return len(queue) == numCourses

        