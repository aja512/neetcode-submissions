class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval

        for i, (s, e) in enumerate(intervals):
            if end < s:
                # new interval fits entirely before this one; the rest is untouched
                res.append([start, end])
                res.extend(intervals[i:])
                return res
            elif start > e:
                # this interval is entirely before the new one
                res.append([s, e])
            else:
                # overlap: grow the merged range
                start = min(start, s)
                end = max(end, e)

        res.append([start, end])
        return res