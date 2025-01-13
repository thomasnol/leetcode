class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # proceed from left to right adding tokens to the stack
        # when an operator is found, pop twice and do the operation, then append res to the stack
        stk = []
        for t in tokens:
            if t == "+" or t == "-" or t == "*" or t == "/":
                n2 = int(stk.pop())
                n1 = int(stk.pop())
                if t == "+": res = n1 + n2
                if t == "-": res = n1 - n2
                if t == "*": res = n1 * n2
                if t == "/": res = int(n1 / n2)
                stk.append(res)
            else:
                stk.append(int(t))
        return stk.pop()