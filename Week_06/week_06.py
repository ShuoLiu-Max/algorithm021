# 爬楼梯
class Solution:
    def climbStairs(self,n:int):
        if n==1:
            return 1
        if n==2:
            return 2
        a=1
        b=2
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return c

# 三角形最小路径和
# 状态转移方程：f(i,j)=min(f(i+1,j),f(i+1,j+1))+triangle[i][j]
# 把所有的情况都遍历一遍，注意每次遍历是在之前的基础之上进行的遍历，所以时间复杂度为O(n^2)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]):
        n = len(triangle)
        f=[[0]*n for n in range(1,n+1)]
        f[0][0] = triangle[0][0]
        for i in range(1,n):
            f[i][0] = f[i-1][0] + triangle[i][0]
            for j in range(1,i):
                f[i][j] = min([f[i-1][j-1],f[i-1][j]]) + triangle[i][j]
            f[i][i] = f[i-1][i-1]+triangle[i][i]
        return min(f[n-1])


# 最大子序列和

class Solution:
    def maxSubArray(self, nums: List[int]):
        dp = nums
        for i in range(1,len(dp)):
            dp[i]=max(dp[i],dp[i]+dp[i-1])
        return max(dp)


#乘积最大子数组

class Solution:
    def maxProduct(self, nums):
        if len(nums)==1:
            return nums[0]
        Fmin = nums.copy() # # 这里不能写成Fmin =nums ; Fmax = nums , 否则Fmin和Fmax指向的同一个地址，改变Fmin后Fmax也会相互影响
        Fmax = nums.copy()
        for i in range(1,len(nums)):
            Fmin[i] = min(Fmax[i-1]*nums[i], Fmin[i-1]*nums[i], nums[i])
            Fmax[i] = max(Fmax[i-1]*nums[i], Fmin[i-1]*nums[i], nums[i])
            pass
        return max(max(Fmin),max(Fmax)) 

Solution().maxProduct([2,3,-2,4])



# 打家劫舍

class Solution:
    def rob(self, nums) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        if len(nums)>=3:
            d = nums.copy()
            d[1]=max(nums[0:2])
            for i in range(2,len(nums)):
                d[i]=max(d[i-1],d[i-2]+nums[i])
            return d[i]


# 打家劫舍II

class Solution:
    def rob(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        d1=nums[0:len(nums)-1].copy()
        d2=nums[1:len(nums)].copy()
        if len(d1)==2:
            return max(max(d1),max(d2))
        if len(d1)>=3:
            d1[1]=max(d1[0:2])
            for i in range(2,len(d1)):
                d1[i]=max(d1[i-1],d1[i-2]+d1[i])
            d2[1]=max(d2[0:2])
            for i in range(2,len(d2)):
                d2[i]=max(d2[i-1],d2[i-2]+d2[i])
            return max(d1[i],d2[i])
print(Solution().rob([1,2,3,1]))

# 买卖股票的最佳时机
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        p_min=[0]*len(prices)
        p_max=[0]*len(prices)
        p_min[0]=prices[0]
        for i in range(1,len(prices)):
            p_min[i]=min(p_min[i-1],prices[i])
            p_max[i]=prices[i]-p_min[i]  # 当前天的股票价格减去之前天（可以包含当前天）的最低价格
        return max(p_max)

# 买卖股票的最佳时机II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        get_price=0
        if len(prices)==1:
            return 0
        for i in range(1,len(prices)):
                get_price+=max(prices[i]-prices[i-1],0)
        return get_price


# 最小路径和

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = grid.copy()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    pass
                elif i==0 and j!=0:
                    g[i][j]+=g[i][j-1]
                elif j==0 and i!=0:
                    g[i][j]+=g[i-1][j]
                else:
                    g[i][j]+=min(g[i][j-1],g[i-1][j])
        return g[-1][-1]



# 解码方法
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n==0: return 0
        dp = [1,0]
        dp[1] = 1 if s[0]!='0' else 0 
        for i in range(1,n):
            dp.append(0)
            if s[i]!='0':
                dp[i+1] += dp[i]
            if s[i-1:i+1]>='10' and s[i-1:i+1]<='26':
                dp[i+1] += dp[i-1]
        return dp[-1]
