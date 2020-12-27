# 岛屿的数量
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return 
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

# 扫雷游戏
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i,j=click
        row=len(board)
        col=len(board[0])
        if board[i][j]=='M':
            board[i][j]='X'
            return board     # 如果点中了地雷，则M变为X,返回面板
        def cal(i,j):
            res=0
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if x==0 and y==0:continue
                    if 0<=i+x<row and 0<=j+y<col and board[i+x][j+y]=='M':
                        res+=1
            return res
        def dfs(i,j):
            num = cal(i,j)
            if num>0:
                board[i][j]=str(num)    #终止条件
                return  
            board[i][j]='B'
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if x==0 and y==0:
                        continue
                    if  0<=i+x<row and 0<=j+y<col and board[i+x][j+y]=='E':dfs(i+x,j+y)    # 地雷M不会被显示，遇到数字也不会再对数字临近的位置进行揭露，只有遇到E时，才会继续递归
        dfs(i,j)
        return board


# 柠檬水找零
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=[0,0,0,0,0]
        for i in bills:
            a[int(i/5)]+=1
            a[int(i/10)]-=1
            a[int(i/20)]-=1    # 贪心算法，先找零10，再找零5
            if (a[1]<0) or (a[1]+2*a[2]<0):    # 使用贪心算法，可以使得5元的零钱剩下的数量达到最多，如果这样5元零钱都不足，那就是肯定无法正确找零。由于判断a[1]<0，是在假设有足够10元数量的情况下得到的，但是实际中10元零钱的数量即a[2]可能是负值，所以这是需要用5元零钱去填补，所以要保证a[1]+2*a[2]>=0才行，否则无法正确找零
                return False
        return True 

# 买卖股票的最佳时机II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        get_price=[0]
        if len(prices)==1:
            return 0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>0:
                get_price.append(prices[i]-prices[i-1])
        return sum(get_price)

# 分发饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_pin=s_pin=count=0  # g指针，s指针，计数
        g_num,s_num=len(g),len(s)
        while (g_pin<=g_num-1) and (s_pin<=s_num-1):
            if g[g_pin]<=s[s_pin]:
                g_pin+=1
                s_pin+=1
                count+=1 
            else:
                s_pin+=1
        return count


# 模拟行走机器人
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions={
            'up':{0:[0,1],-1:'right',-2:'left'},
            'down':{0:[0,-1],-1:'left',-2:'right'},
            'left':{0:[-1,0],-1:'up',-2:'down'},
            'right':{0:[1,0],-1:'down',-2:'up'}
            }
        obstacles = set(map(tuple,obstacles))
        current_direction='up'
        coordinate=[0,0]
        res=0
        for com in commands:
            if com<0:
                current_direction = directions[current_direction][com]
            else:
                for i in range(1,com+1):
                    tmp_x, tmp_y = coordinate[0],coordinate[1]
                    tmp_x+=directions[current_direction][0][0]
                    tmp_y+=directions[current_direction][0][1]
                    if (tmp_x,tmp_y) in obstacles:
                        break
                    coordinate=[tmp_x, tmp_y]
                res = max(res, coordinate[0]**2+coordinate[1]**2)
        return res

# 搜索旋转排序数组
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==[]:return -1
        l=0
        r=len(nums)-1
        while l<r:
            mid=(r+l)//2
            if nums[mid]<nums[r]:  #右边大部分是较小的一部分数
                if nums[mid]<target<=nums[r]:  
                    l=mid+1
                else:r=mid
            else:   # 左边大部分是较大的一部分数
                if nums[l]<=target<=nums[mid]:
                    r=mid
                else:l=mid+1
        if nums[l]==target:return l
        else:return -1


