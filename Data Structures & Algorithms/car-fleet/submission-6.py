class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we can make a stack that contains cars speed first, position second 
        # we can order the stack by position, with last being at the end
        # then we need to make use of the TIME it takes for each position car to get to the target
        # if the car IN FRONT of the last takes longer than the car behind it, pop the car behind it, and so on.
        stack = []
        pairs = []
        for p, s in zip(position, speed):
            t = (target - p) / s # time
            pairs.append([p, t])
        # sort the stack
        pairs.sort(reverse=True)
        for p in pairs:
            stack.append(p)
            if len(stack) >= 2 and stack[-1][1] <= stack[-2][1]:
                stack.pop()
        return len(stack)
