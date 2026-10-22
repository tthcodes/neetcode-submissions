class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize a hmap that the values will contain a list of prereqs. this will be from 0 -> numCourse
        preMap = {i : [] for i in range(numCourses)}

        # iterate through prereqs
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # we're gonna need a set that tells us if we're currently taking the course as we traverse through what's possible to take
        attending = set()

        # we need to make sure that we can complete all the prereqs, before the course. dfs approach
        def dfs(crs):
            if crs in attending: # if we're currently attending the course, return false early 
                return False 
            # then we add it to attend 
            attending.add(crs)

        # if we're not currently attending it, check if we can attend each of its pre-preqs
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False 
            
            # if we make it through and we can attend every pre and current crs, take out of taking
            attending.remove(crs)
            
            # set crs pre reqs to empty since we know it's possible to attend
            preMap[crs] = [] 
            
            # return true 
            return True 
                
        # we need to iterate over the preMap, and call dfs on it 
        for crs in preMap:
            if not dfs(crs):
                return False

        return True 
