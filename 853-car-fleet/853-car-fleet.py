class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted([[p,s] for p,s in zip(position,speed)])
        stack = []
        #time = (target - position)/speed
        for p,s in pair[::-1]:
            t = (target - p)/s
            if stack and t <= stack[-1][2]:
                continue
            else:
                stack.append([p, s, t])
        return len(stack)
                    
            