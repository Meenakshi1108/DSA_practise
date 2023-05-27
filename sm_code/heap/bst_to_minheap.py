class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


def insert_bst(root,key):
	if root is None:
		root=Node(key)
		return root
	if root.data>key:
		root.left=insert_bst(root.left,key)
	elif(root.data<key):
		root.right=insert_bst(root.right,key)
	return root

# buildabst,get inorder,do the preorder of the inorder to get the minheap

def inorder(root,v):
	if root is None:
		return 

	inorder(root.left,v)
	v.append(root.data)
	inorder(root.right,v)
	return v

def preorder(root,v):
	if root is None:
		return 
	root.data=v.pop(0)
	preorder(root.left,v)
	preorder(root.right,v)

def bst_to_minheap(arr,root):
	n=len(arr)
	v=[]
	v=inorder(root,v)
	preorder(root,v)

def printlevelorder(root):
	if root is None:
		return

	q=[]
	q.append(root)
	while(q):
		curr=q.pop(0)
		print(curr.data,end=" ")
		if curr.left:
			q.append(curr.left)
		if curr.right:
			q.append(curr.right)
	print()

if __name__=="__main__":
	arr=list(map(int,input().split()))
	root=None
	for i in arr:
		if i!=-1:
			root=insert_bst(root,i)
	bst_to_minheap(arr,root)
	printlevelorder(root)


