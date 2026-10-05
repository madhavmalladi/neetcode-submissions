class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_reqs = defaultdict(list)
        for course, pre_req in prerequisites:
            pre_reqs[course].append(pre_req)

        visiting = set()

        def dfs(course):
            if course in visiting: # there is a cycle
                return False
            if pre_reqs[course] == []: # no prereqs
                return True

            visiting.add(course)
            for pre_req in pre_reqs[course]:
                if not dfs(pre_req):
                    return False
            
            pre_reqs[course] = []
            visiting.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True