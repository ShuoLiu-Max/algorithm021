# 学习笔记：
## 1、深度优先DFS代码模板：python
### 递归写法：
```
visited = set()
def dfs(node,visited):
    if node in visited:   #terminator
        # already visited
        return
    visited.add(node)
    #process current node here
    # ...
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node,visited)
```
### 非递归写法：(使用栈)
```
def DFS(self,tree):
    if tree.root is None:
        return []
    visited, stack = [], [tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
```


## 广度优先BFS代码模板：python
### 非递归写法：（使用队列）
```
def BFS(graph,start,end):
    visited = set()
    queue = []
    queue.append([start])
    while queue:
        node = queue.pop(0)
        visited.add(node)
        process(node)
        node = generate_related_nodes(node)
        queue.push(nodes)
    #other processing work
```

# 2、二分查找的条件：单调、存在边界
## 二分查找代码模板：
```
left=0
right=len(array)-1
while left<=right:
	mid = (left+right)/2
	if array[mid]==target:
		#find the target！
		break or return result
	elif array[mid]<target:
		left = mid+1
	else:
		right = mid-1
```
