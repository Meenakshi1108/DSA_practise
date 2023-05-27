k=-1

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



def kth_largest(root):
	global k
	if root is None:
		return None

	right =kth_largest(root.right)
	if(right is not None):
		return right
	k-=1

	if(k==0):
		return root
	return kth_largest(root.left)


def kth_smallest(root):
	global k
	if root is None:
		return None

	left=kth_smallest(root.left)
	if left is not None:
		return left

	k-=1

	if(k==0):
		return root

	return kth_smallest(root.right)


t = int(input())
for i in range(t):
    n = int(input())
    keys = list(map(int, input().split()))
    k=int(input())
    temp=k
    root = None
    for key in keys:
        if key!=-1:
            root = insert_bst(root, key)

    l=kth_largest(root)
    print(l.data)
    k=temp
    s=kth_smallest(root)
    print(s.data)

