class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = zip(position, speed)
        #pair them up
        pairs = sorted(pairs)
        #sort them
        stack = []
        #loop through reverse because closer to target goes first
        for p,s in pairs[::-1]:
            t = (target - p) / s
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            
            
        
        # 12 = speed(x) + position
        # (target - position) / speed = x