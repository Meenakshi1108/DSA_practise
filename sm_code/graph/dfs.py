import collections
class Graph:
	def __init__(self,adj_list):
		self.adj_list=adj_list

	def dfs_iter(self,root):
		visited=[False for i in range(len(self.adj_list))]
		stack=[]
		stack.append(root)
		while len(stack):
			root=stack[-1]
			stack.pop()
			if(not visited[root]):
				print(root,end=" ")
				visited[root]=True

			for neighbour in self.adj_list[root]:
				if(not visited[neighbour]):
					stack.append(neighbour)

	def dfs_recur(self,root,visited):

		visited.add(root)
		print(root,end=' ')

		for neighbour in self.adj_list[root]:
			if neighbour not in visited:
				self.dfs_recur(neighbour,visited)




n=int(input())
adjlist={}
for i in range(n):
	key=int(input())
	value=list(map(int,input().split()))
	adjlist[key]=value 
root=0

input1=Graph(adjlist)
input1.dfs_iter(root)
