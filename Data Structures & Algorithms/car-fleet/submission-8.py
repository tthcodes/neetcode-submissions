class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        input: 2 int arrays, one being position of ith car, second being speed of ith car, 1 int, target position
        output: int, number of fleets 

        car fleet is set of cars driving same position and speed

        if car catches up to fleet same moment it reaches dest, car considered part of that fleet. 

        need to calculate time it takes to get to destination, while also considering the position. if the time it takes for a car BEHIND another one is greater, it needs to become part of the fleet ahead of it.


        we can imp a stack, and WHILE the time it takes for the top of the stack is LESS THAN the current time fleet, we pop it off as if it belongs to current. 

        then we return the length of the stack to reference diff fleets

        the challenge is that we need to combine the two lists and then ORDER them by position before we think about fleet assignment
        '''

        stack = []

        positionAndTime = []
        # use zip to account for 2 arrays 

        for p, s in zip(position, speed):
            time = (target - p) / s
            positionAndTime.append((p, time))
        
        for p, t in sorted(positionAndTime):
            while stack and stack[-1][1] <= t:
                stack.pop()
            stack.append((p, t))
        
        return len(stack)
