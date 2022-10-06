class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval] 
        p_start, p_end = intervals[0][0], intervals[0][1]
        n_start, n_end = newInterval[0], newInterval[1]
        print(n_start, n_end)
        overlap = []
        resint = ["X", "X"]
        i = 0
        for i in range(len(intervals)):
            print("i", i)
            start = intervals[i][0]
            end = intervals[i][1]
            if n_start > end:
                continue
            # if n_start <= end and n_end <= end:
            #     print("thisreturn", n_start, n_end, start, end)
                # return intervals
            if start<= n_start <= end or start<= n_end <= end or n_start <= start <= end <= n_end:
                overlap.append(i)
        if overlap == []:
            intervals = sorted(intervals + [newInterval])
            return intervals
        resint = [min(n_start, intervals[overlap[0]][0]), max(n_end, intervals[overlap[-1]][1])]
        print("overlap", overlap)
        print("resint", resint)
#                 resint[0] = start
#                 if end > n_end:
#                     i += 1
#                 else:
#                     while end <= n_end:
#                         overlap.append(i)
#                         resint[1] = n_end
#                         i += 1
#                         start = intervals[i][0]
#                         end = intervals[i][1]
#                 print(resint)
#             else:
#                 i += 1
                
        print(overlap)
        # if len(overlap) == 1:
        #     intervals[overlap[0]] = resint
        #     return intervals
        intervals = intervals[:overlap[0]] + [resint] + intervals[overlap[-1] + 1:]
        return intervals
        
                    
                
                
                
            
                
        