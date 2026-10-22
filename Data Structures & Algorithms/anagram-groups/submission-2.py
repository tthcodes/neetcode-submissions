class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize a default dict that ALREADY has lists as values
        anaMap = defaultdict(list)
        # iterate over collection of strs
        for s in strs:
            # init a blank list of 0's
            anaGroup = [0] * 26
            # iterate over chars for each s and update anaGroup
            for c in s:
                anaGroup[ord(c) - ord('a')] += 1
            # append the curr s to proper anaGroup it belongs to
            anaMap[tuple(anaGroup)].append(s)
        return list(anaMap.values())
