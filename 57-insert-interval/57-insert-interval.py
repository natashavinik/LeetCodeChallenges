class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval] 
        p_start, p_end = intervals[0][0], intervals[0][1]
        n_start, n_end = newInterval[0], newInterval[1]
        overlap = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if n_start > end:
                continue
            if start<= n_start <= end or start<= n_end <= end or n_start <= start <= end <= n_end:
                overlap.append(i)
        if overlap == []:
            intervals = sorted(intervals + [newInterval])
            return intervals
        resint = [min(n_start, intervals[overlap[0]][0]), max(n_end, intervals[overlap[-1]][1])]
        intervals = intervals[:overlap[0]] + [resint] + intervals[overlap[-1] + 1:]
        return intervals
        
                    
                
                
                
            
                
        