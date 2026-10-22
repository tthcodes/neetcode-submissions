class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # init your result to match to result length of temps
        res = [0] * len(temperatures)
        # iterate over the temperatures to hold temp and index, always append 
        # init a stack 
        stack = []
        for i, t in enumerate(temperatures):
            # while the stack is NOT empty and last temp is lower than current, update
            while stack and stack[-1][1] < t:
                # first index will be index, second will be temp
                ind, temp = stack.pop()
                # update the index num to be the time between last and cur index
                res[ind] = i - ind
            # append the current ind, temp
            stack.append([i, t])
        return res