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

def search(root,key):
	while(root):

		
		if(key<root.data):
			root=root.left
		elif(key>root.data):
			root=root.right
		elif root.data==key:
			print("Element Found")
			return True
		else:
			return False
	return False

t = int(input())
for i in range(t):
    n = int(input())
    keys = list(map(int, input().split()))
    root = None
    for key in keys:
        root = insert_bst(root, key)
    search(root,4)