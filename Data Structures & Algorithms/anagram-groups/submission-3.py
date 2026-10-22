class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can populate a word letter count using a list 0 -> 25 representing a-z 
        # dict to group anagrams together
        grouped = defaultdict(list)

        for s in strs:
            anagram = [0] * 26
            for c in s:
                anagram[ord(c) - ord('a')] += 1
            grouped[tuple(anagram)].append(s)
        
        return list(grouped.values())