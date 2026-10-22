class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # input: list of integers
        # output: concat of two nums arrays, a double of the input
        ans = []
        count = 2
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
