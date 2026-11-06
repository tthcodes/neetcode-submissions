class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        begin 2 pointers at each end, if their sum is greater than target, bring down right side, if sum is lesser, bring up left side. once target is matched to sum, return left and right indices + 1
        '''
        l, r = 0, len(numbers) - 1

        # since they cannot be same number used twice, while loop is l < r
        while l < r:
            total = numbers[l] + numbers[r]
            if target > total:
                l += 1
            elif target < total:
                r -= 1
            else:
                return [l + 1, r + 1]
