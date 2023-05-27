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

def height(node):
	if node is None:
		return 0
	return max(height(node.left),height(node.right))+1

def is_balanced(root):
	if root is None:
		return True

	lh=height(root.left)
	rh=height(root.right)

	if (abs(lh-rh)<=1) and is_balanced(root.left) is True and is_balanced(root.right) is True:
		return True

	return False


t = int(input())
for i in range(t):
    n = int(input())
    keys = list(map(int, input().split()))
    root = None
    for key in keys:
    	if(key!=-1):
    		root = insert_bst(root, key)
    print(root.data)
    # inorder(root)
    if is_balanced(root):
    	print("Tree is balanced")
    else:
    	print("Tree is not balanced")