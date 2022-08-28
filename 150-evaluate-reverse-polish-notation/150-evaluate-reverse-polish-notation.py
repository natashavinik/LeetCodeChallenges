class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in ["*", "+", "-", "/"]:
                stack.append(c)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if c == "*":
                    stack.append(first * second)
                elif c == "+":
                    stack.append(first + second)
                elif c == "-":
                    stack.append(first - second)
                else:
                    stack.append(int(first / second))
        return stack[0]
            