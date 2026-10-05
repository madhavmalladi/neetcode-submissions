class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list of prereqs
        prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        ans = []
        visited = set()
        curr_path = set()

        def dfs(course):
            if course in curr_path: # we have a cycle
                return False
            if course in visited: # don't need to visit again
                return True
            
            curr_path.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq): # there is a cycle
                    return False
            
            visited.add(course)
            curr_path.remove(course)
            ans.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return ans
            