class Solution:
    def decodeString(self, s: str) -> str:
        # single stack solution
        # go from left to right side
        # for c in s:
        # if c != ']':
        # add to stack
        # else:
        # while stack.pop != '['
        # pop stack 1 more time for the bracket
        # extract multi-digit number
        # push back into stack the multiplied string

        stack = []
        for c in s:
            curstring = ''
            if c != ']':
                stack.append(c)
            else:
                curstring = ''
                while stack[-1] != '[':
                    curstring = stack.pop() + curstring
                stack.pop()
                mult = ''
                while stack and stack[-1].isdigit():
                    mult = stack.pop() + mult
                curstring *= int(mult)
                stack.append(curstring)
        return "".join(stack)
        