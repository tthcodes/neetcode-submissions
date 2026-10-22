class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # the difference between target and position, divided by speed. gives us time it takes to get there
        # and if the time of the previous top of the stack is < what is being added, pop it. 
        stack = []
        # need to order cars by position, decreasing order so that those closest to target are first
        cars = sorted(zip(position, speed), reverse=True)
        for pos, spd in cars:
            distance = target - pos
            time = distance / spd
            # ONLY if the stack is EMPTY.. OR the current time is BIGGER than time before do u add
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)