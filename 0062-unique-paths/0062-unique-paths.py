class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # lookup = {}
        # res = 0
        # while(m > 0 and n > 0):
        #     if m == 1 or n == 1:
        #         res += 1
            
        #     if (m, n) in lookup:
        #         res += lookup[(m, n)]
            
        #     down = f(m - 1, n)
        #     right = f(m, n - 1)

        #     lookup[(m, n)] = down + right

        #     res += down + right
        
        # return res




        # +1+2+...+6+n with n=7
        dp = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(1)
            dp.append(temp)
        print(dp)

        for i in range(1, m):
            for j in range(1, n):
                up = dp[i - 1][j]
                left = dp[i][j - 1]
                dp[i][j] = up + left
        
        return dp[m-1][n-1]



        # lookup = {}
        # def f(m, n):
        #     if m == 1 or n == 1:
        #         return 1
            
        #     if (m, n) in lookup:
        #         return lookup[(m, n)]
            
        #     down = f(m - 1, n)
        #     right = f(m, n - 1)

        #     lookup[(m, n)] = down + right

        #     return down + right
        
        # return f(m, n)