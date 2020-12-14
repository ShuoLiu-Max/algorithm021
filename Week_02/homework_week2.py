# 有效的字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        for i in s:
            if i in dict_s:
                dict_s[i]+=1
            else:
                dict_s[i]=1
        for i in t:
            if i in dict_t:
                dict_t[i]+=1
            else:
                dict_t[i]=1
        if dict_s==dict_t:
            return True
        else:return False



# 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        haxi={}
        for i ,num in enumerate(nums):
            haxi[num] = i
        for i,num in enumerate(nums):
            if (haxi.get(target-num) is not None) & (haxi.get(target-num)!=i):    #字典.get(key)返回值，如果没有该键则返回None
                return [i,haxi[target-num]]

# N叉树的前序遍历
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        if not root:
            return res
        stack=[root]
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            stack.extend(temp.children[::-1])
        return res

# 字母异位词分组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            key = tuple(sorted(i))
            dict[key] = dict.get(key,[])+[i]
        return list(dict.values())

# 二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        white, gray = 0, 1
        res = []
        stack = [(white, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == white:
                stack.append((white, node.right))
                stack.append((gray, node))
                stack.append((white, node.left))
            else:
                res.append(node.val)
        return res

# 二叉树的前序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        white, gray = 0, 1
        res = []
        stack = [(white, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == white:
                stack.append((gray, node))
                stack.append((white, node.right))
                stack.append((white, node.left))
            else:
                res.append(node.val)
        return res

# N叉树的层序遍历
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            res.append(node.val for node in queue)
            queue = [child for node in queue for child in node.children]
        return res


# 丑数
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 =0
        while n>1:
            u2, u3, u5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            n -= 1
            ugly.append(umin)
        return ugly[-1]

# 前k个高频元素
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans