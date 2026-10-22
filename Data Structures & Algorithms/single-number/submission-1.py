class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return an int
        # we can use bit manipulation here, which gives us constant space soluition, and linear time.
        n = 0 # since using XOR with 0 will give you either 0 if other number is 0 or the other X number itself 
        for num in nums:
            n ^= num 
        return n
