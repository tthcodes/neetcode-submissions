class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       # for each node, can we complete the course or not? 
       # DFS for exploring dependencies and detecting cycles 
       # utilize a hashmap and a set() 
       # TOPOLOGICAL SORT 
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # these represents that courses that we're CURRENTLY VISITING/TAKING. 
        # this is used so that if we find a PRE-REQ that is already being visited, that's a LOOP
        visited = set()

        # we can run DFS on each course from 0 -> numCourses for each of its pre
        def dfs(crs):
            # we want to check all of the prereqs for this current course and return false if 
            if crs in visited:
                return False
            
            if preMap[crs] == []:
                return True
            
            #add to visited
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): # if we find one course that can't be completed, false for whole function
                    return False 

            # now we know all pre-reqs can be done, remove this crs from visited    
            visited.remove(crs)

            # set prereq to empty list since we already know all pre reqs can be done
            preMap[crs] = []
            return True 
            


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


    