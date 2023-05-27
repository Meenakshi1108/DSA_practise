class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_bst(root,key):

    if root is None:
        root=Node(key)
        return root
    else:
        if key<root.data:
            root.left=insert_bst(root.left,key)
        else:
            root.right=insert_bst(root.right,key)
                
    return root
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def lca_recursive(root,x,y):
	if root is None:
		return None
	if root.data<x and root.data<y:
		return lca_recursive(root.right,x,y)
	if root.data>x and root.data>y:
		return lca_recursive(root.left,x,y)
	return root

t = int(input())
for i in range(t):
    n = int(input())
    keys = list(map(int, input().split()))
    root = None
    for key in keys:
    	if(key!=-1):
    		root = insert_bst(root, key)
    print("root is",root.data)
    x=3
    y=5
    inorder(root)
    print()
    lca=lca_recursive(root,x,y)
    print("LCA of",x,"and",y,"is",lca.data)