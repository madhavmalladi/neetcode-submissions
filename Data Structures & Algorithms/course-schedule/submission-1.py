class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_reqs = defaultdict(list)
        for course, pre_req in prerequisites:
            pre_reqs[course].append(pre_req)
        
        visiting = set()

        def dfs(course_num):
            if course_num in visiting: # there is a cycle
                return False 
            if pre_reqs[course_num] == []:
                return True
            
            visiting.add(course_num)
            for pre_req in pre_reqs[course_num]:
                if not dfs(pre_req):
                    return False
            
            # at this point, this course is able to be taken
            pre_reqs[course_num] = []
            visiting.remove(course_num)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
        