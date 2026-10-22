class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visiting:
                return False
            
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)

            preMap[crs] = []

            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return False 
        
        return True