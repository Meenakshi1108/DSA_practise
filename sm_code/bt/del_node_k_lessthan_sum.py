class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildtree(arr):
    n = len(arr)
    if n == 0:
        return None
    root = None
    for j in range(n):
        if arr[j] != -1:
            root = Node(arr[j])
            break
    q = [root]
    k = j + 1
    while q:
        node = q.pop(0)
        if k < n:
            if arr[k] != -1:
                node.left = Node(arr[k])
                q.append(node.left)
            k += 1
        if k < n:
            if arr[k] != -1:
                node.right = Node(arr[k])
                q.append(node.right)
            k += 1
    return root

def inorder(root):
	if root is None:
		return 
	inorder(root.left)
	print(root.data,end=" ")
	inorder(root.right)

def sum_path(root,sum):
	if root is None:
		return None

	root.left=sum_path(root.left,sum-root.data)
	root.right=sum_path(root.right,sum-root.data)

	if (root.left is None and root.right is None):
		if(sum>=root.data):
			return None

	return root

t = int(input())
for i in range(t):
    # n = int(input())
    arr = list(map(int, input().split()))
    root = buildtree(arr)
    # Do something with the tree here, like print its elements.
    inorder(root)
    root=sum_path(root,20)
    print()
    inorder(root)
