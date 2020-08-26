# https://leetcode.com/problems/merge-intervals/solution/
 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) is 0:
            return []
        
        intervals.sort()
        ret_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            a, b = ret_intervals[-1]
            c, d = intervals[i]
            if b < c:
                ret_intervals.append([c, d])
            elif c <= b < d:
                ret_intervals[-1] = [a, d]
            else:
                continue
        
        return ret_intervals