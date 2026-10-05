class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_reqs = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre_reqs[course].append(prerequisite)
        
        # current dfs path
        visiting = set()

        def dfs(course):
            if course in visiting: # there is a cycle detected
                return False
            if pre_reqs[course] == []: # no pre-reqs for this course
                return True
            
            visiting.add(course)
            for pre_req in pre_reqs[course]:
                if not dfs(pre_req):
                    return False
            visiting.remove(course)
            
            '''
            we clear the pre-reqs of the course to mark it as done, as we
            know that this course is able to be taken
            '''
            pre_reqs[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
                