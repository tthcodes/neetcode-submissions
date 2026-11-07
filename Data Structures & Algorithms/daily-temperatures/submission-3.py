class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        input: int list (temp), each int represents temp on ith day
        output: int list, where result[i] is # of days after ith day before WARMER temp will appear. 

        init a res = int list, where all nums init at 0. 
        iterate over temps and push the current i, n onto the stack IF stack doesn't yet exist OR while the top of the stack is GREATER than current n. 
        IF the current n is GREATER than top of the stack, you pop off top of stack and update top i's res num to curr i - num i. 
        then you return res 
        '''

        res = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            if not stack:
                stack.append([i, n])
                continue
            while stack and stack[-1][1] < n:
                topInd, topVal = stack.pop()
                res[topInd] = i - topInd 
            stack.append([i, n])
        return res

