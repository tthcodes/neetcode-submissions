class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # logic is you need to hold on to both the day/index and the temperature 
        # create a stack and only add on when there is a temp higher 
        # iterate over using enumerate 
        stack = [] 
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append([i, t])
            if stack and stack[-1][1] >= t:
                stack.append([i, t])
            elif stack[-1][1] < t:
                while len(stack) != 0 and stack[-1][1] < t:
                    lastInd, lastTemp = stack.pop()
                    res[lastInd] = i - lastInd
                stack.append([i, t])
        return res