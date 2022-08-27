class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        #pushes val on stack
        self.stack.append(val)
        if self.minstack == []:
            self.minstack.append(val)
        elif self.minstack[-1] < val:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)
        # print("Val", val, "stack", self.stack, "minstack", self.minstack)

    def pop(self) -> None:
        #removes top element from stack
        self.stack.pop()
        self.minstack.pop()
        # print("pop stack", self.stack, "pop minstack", self.minstack)
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        # print(self.stack)
        # print(self.minstack)
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()