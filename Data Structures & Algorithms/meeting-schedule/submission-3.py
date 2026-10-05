"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prevEnd = 0
        intervals = sorted(intervals, key=lambda x: x.start)
        for interval in intervals:
            if (interval.end < prevEnd):
                return False
            elif (interval.start < prevEnd):
                return False
            prevEnd = interval.end
        return True