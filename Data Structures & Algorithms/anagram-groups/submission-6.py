class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        strs[i] all lowercase english, so we can create an int list to serve as hmap key
        for each word, and if there's a match that exists, we append it to value list

        defaultdict as list

        init a res list 

        for every word we need it make sure it's added to the list even if it's a blank. OR what we can do is if the length of stres is ever just 1, we add that to resulting list 
        '''
        res = []

        groupedAnagrams = defaultdict(list)

        for s in strs:
            key = [0] * 26
            
            for c in s:
                key[ord(c) - ord('a')] += 1
            
            groupedAnagrams[tuple(key)].append(s)
            
        return list(groupedAnagrams.values())