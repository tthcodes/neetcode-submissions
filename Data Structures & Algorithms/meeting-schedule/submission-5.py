"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # input is an array of meeting time intervals, list of lists. 
        # output is a boolean, determining if person can a†tend ALL meetings. (no 2 overlap)
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            previousEnd = intervals[i - 1].end
            nextStart = intervals[i].start
            if previousEnd > nextStart:
                return False
        return True 
