import collections
class Graph:
	def __init__(self,adj_list):
		self.adj_list=adj_list

	def bfs(self,root):
		visited=set()
		queue=collections.deque([root])
		visited.add(root)
		while queue:
			vertex=queue.popleft()
			print(str(vertex),end=" ")
			
			for neighbour in self.adj_list[vertex]:
				if neighbour not in visited:
					
					visited.add(neighbour)
					queue.append(neighbour)


# n=int(input())
# adjlist={}
# for i in range(n):
# 	key=int(input())
# 	value=list(map(int,input().split()))
# 	adjlist[key]=value 
# root=int(input())
adjlist = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
input1=Graph(adjlist)
input1.bfs(0)
