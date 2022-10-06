class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
            
        s_int = sorted(intervals)
        pre_start = s_int[0][0]
        pre_end = s_int[0][1]
        for i in range(1, len(s_int)):
            start = s_int[i][0]
            end = s_int[i][1]
            if pre_end <= start:
                pre_end = end
                continue
            else:
                return False
        return True
        