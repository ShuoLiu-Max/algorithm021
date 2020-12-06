"""
1.用 add first 或 add last 这套新的 API 改写 Deque 的代码
Dequedeque = new LinkedList();
deque.addLast("a");
deque.addLast("b");
deque.addLast("c");
System.out.println(deque);

String str = deque.peekFirst();
System.out.println(str);
System.out.println(deque);

while(deque.size()>0){
System.out.println(deque.removeFirst())
}
System.out.println(deque);

2.分析Queue和Priority Queue的源码
python的简单分析：
Queue:
1.python的queue在lib/queue.py文件中，定义了Queue的类

2.从__init__函数来看，python的queue初始化会创建一个deque，可传入的参数为maxsize，即为队列的最大长度，同时初始化的属性有self.maxsize（队列最大长度）
self.mutex（线程锁）self.not_empty，self.not_full， self.all_tasks_done三个属性用于线程的控制，还有一个self.unfinished_tasks默认为0
由于封装了线程锁，所以python的queue是线程安全的

3.put方法：
往队列里添加元素会调用put方法，put方法包含三个参数，第一个是传入的元素，第二个block是是否存在锁，第三个timeout是用来控制等待时间的。
首先会检查是否被锁住，如果锁存在，那么会等待锁的释放，直到等待时间超过设定的timeout，如果未设定timeout，会一直等待。
如果没有锁住，那么会检查当前队列的长度是否大于等于设定的最大长度，如果小于最大长度，那么执行deque的append操作，将元素插入队列，同时将self.unfinished_tasks加一
def put(self, item, block=True, timeout=None):
with self.not_full:
if self.maxsize > 0:
if not block:
if self._qsize() >= self.maxsize:
raise Full
elif timeout is None:
while self._qsize() >= self.maxsize:
self.not_full.wait()
elif timeout < 0:
raise ValueError("'timeout' must be a non-negative number")
else:
endtime = time() + timeout
while self._qsize() >= self.maxsize:
remaining = endtime - time()
if remaining <= 0.0:
raise Full
self.not_full.wait(remaining)
self._put(item)
self.unfinished_tasks += 1
self.not_empty.notify()

4.get方法与put方法流程类似，取出元素时调用了popleft方法
5.如果是单线程任务，可以使用put_nowait和get_nowait方法，这俩方法也是用put和get实现的，只不过参数block为False，无需等待锁的释放
6.qsize方法会返回队列的长度，底层使用的是len()方法，empty方法是查看len()方法是否返回的是0，full方法则会查看当前队列的长度是否已经大于等于设定的最大长度

Priority Queue
1.python的优先队列是用堆结构实现的，主要的方法都在lib/heapq.py代码中，源码中PriorityQueue类继承了Queue类，但不同的是初始化会不再是创建一个deque，而是直接创建一个空的list。
2.put和get方法直接调用了heappush和heappop
3.heapq模块的实现较为深奥和繁琐
主要分为以下几点：
①heapq模块主要使用了python列表的最小堆排序算法
②添加元素使用了heappush方法，先将元素append进列表，即放在了列表的最尾部，然后再调用_siftdown()方法进行上浮，这里其实就是一个堆排序的过程，通过 newitem 不断与父节点比较，这里用了位运算取代了除以 2 的操作，位运算毕竟更快。不一样的是这里缺少了元素交换的过程，而是计算出新元素最后所在的位置 pos 并进行的赋值。显然这是优化后的代码，减少了不断交换元素的冗余过程。

def _siftdown(heap, startpos, pos):
newitem = heap[pos]
while pos > startpos:
parentpos = (pos - 1) >> 1
parent = heap[parentpos]
if newitem < parent:
heap[pos] = parent
pos = parentpos
continue
break
heap[pos] = newitem

③删除元素使用了heappop方法，通过heap.pop()获得列表中最后一个元素，然后替换为堆顶，再进行下沉
def heappop(heap):
lastelt = heap.pop()
if heap:
returnitem = heap[0]
heap[0] = lastelt
_siftup(heap, 0)
return returnitem
return lastelt
"""


# 删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=0
        b=1
        for _ in range(len(nums)-1):
            if nums[a]==nums[b]:
                b+=1
            else:
                a+=1
                nums[a]=nums[b]
                b+=1
        return a+1

# 旋转数组：
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop()

#合并两个有序链表
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1, temp2 = [], [] 
        f1, f2 = l1, l2 
        while f1:
            temp1.append(f1.val)
            f1 = f1.next
        while f2:
            temp2.append(f2.val)
            f2 = f2.next
        temp = temp1 + temp2
        temp.sort()
        dummy = ff = ListNode(0)
        for i in temp:
            ff.next = ListNode(i)
            ff = ff.next
        return dummy.next


# 合并两个有序数组
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        nums1.sort()
        return nums1

# 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        haxi={}
        for i,num in enumerate(nums):
            haxi[num] = i
        for i,num in enumerate(nums):
            if (haxi.get(target-num) is not None) & (haxi.get(target-num)!=i):    #字典.get(key)返回值，如果没有该键则返回None
                return [i,haxi[target-num]]

# 移动零
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[pos] = nums[pos],nums[i]
                pos += 1

# 加一
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if 9 != digits[-1]:
            digits[-1]=digits[-1]+1
            return digits
        leng = len(digits)
        for i in range(-1,-leng-1,-1):
            if digits[i]==9:
                digits[i]=0
            else: break
        if i>-leng:
            digits[i]=digits[i]+1
        elif digits[i]==0:
            digits.insert(0,1)
        else: digits[i]=digits[i]+1
        return digits

# 设计循环双端队列
class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.list=[]
        self.len=k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.list)<self.len:
            self.list=[value]+self.list
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.list)<self.len:
            self.list.append(value)
            return True
        else:
            return False
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.list):
            del self.list[0]
            return True
        else:return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.list:
            del self.list[-1]
            return True
        else:return False        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.list[0]
        


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.list[-1]
        


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.list:
            return False
        else:
            return True


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.list)==self.len:
            return True
        else:return False

# 接雨水
class Solution:
    def trap(self, height: List[int]) -> int:
        SUM=sum(height)
        temp=[]
        if height==[]:
            return 0
        MAX=max(height)
        k=0
        j = n = len(height)-1
        count=0
        # for i in range(1,MAX+1):
        while MAX:
            for k in range(k,n):
                if height[k]<=count:
                    k+=1
                else: break
            for j in range(j,0,-1):
                if height[j]<=count:
                    j-=1
                else: break
            MAX-=1
            count+=1
            temp.append(j-k+1)
        return sum(temp)-SUM



