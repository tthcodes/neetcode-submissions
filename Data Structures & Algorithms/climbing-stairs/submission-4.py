class Solution:
    def climbStairs(self, n: int) -> int:
        # naive solution would be to use fibonacci
        one, two = 1, 1
        for i in range(n):
            temp = one
            one = one + two
            two = temp

        return two