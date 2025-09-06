class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # is wildcard mode setting?
        # do a for loop, not sure if it should iterate based on s or p.
        # .* should not be greedy, because sometimes we need to cover fewer characters in order to successfully match the string
        # same for the a* and such
        # we will split the problem, either choosing to cover with it or not
        # return value is True/False
        @cache
        def f(s_idx, p_idx, mem):
            
            # if p[p_idx] != "*":
            #     mem = p[p_idx]
            
            # need to look ahead
            while p_idx + 1 < len(p) and p[p_idx + 1] == "*":
                mem = p[p_idx]
                p_idx += 1
                print("MEM SET:", mem)
            
            # base case
            if s_idx >= len(s) and p_idx >= len(p):
                print("BRANCH TRUE:", s_idx, p_idx, mem)
                return True
            
            if p_idx < len(p) and p[p_idx] == "*":
                print("Any match:", s_idx, p_idx, mem)
                if s_idx < len(s) and (mem == s[s_idx] or mem == "."):
                    return f(s_idx, p_idx + 1, mem) or f(s_idx + 1, p_idx, mem) or f(s_idx + 1, p_idx + 1, mem)
                else:
                    return f(s_idx, p_idx + 1, mem)
            
            if s_idx >= len(s) or p_idx >= len(p):
                return False

            if (p[p_idx].isalpha() and s[s_idx] == p[p_idx]) or p[p_idx] == ".":
                print("Standard match:", s_idx, p_idx, mem)
                return f(s_idx + 1, p_idx + 1, mem)
            
            
            return False
        return f(0,0,"X")