class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram = str that contains exact same characters of another string, any order
        # multiple hash maps? 
        strStore = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            strStore[tuple(key)].append(s)
        parentArr = []
        for val in strStore.values():
            parentArr.append(val)
        return parentArr

            
