class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        #3 lists for negatives, positives and zeros
        n, p, z = [], [], []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        #sets for faster access
        N, P = set(n), set(p)
        
        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
        if len(z) >= 3:
            res.add((0, 0, 0))
        # check complements of all pairs of n against P
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                t = -(n[i] + n[j])
                if t in P:
                    res.add(tuple(sorted([n[i], n[j], t])))
        # check complements of all pairs of p against N
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                t = -(p[i] + p[j])
                if t in N:
                    res.add(tuple(sorted([p[i], p[j], t])))
        
        return sorted(res)