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

def height(root):
	if root is None:
		return 0
	lh=height(root.left)
	rh=height(root.right)

	return max(lh,rh)+1

def levelordertraversal(root):
	h=height(root)
	for i in range(1,h+1):
		printlevel(root,i)

def printlevel(root,level):
	if root is None:
		return None
	if level==1:
		print(root.data,end=" ")
	elif(level>1):
		printlevel(root.left,level-1)
		printlevel(root.right,level-1)

	return 



t = int(input())
for i in range(t):
    # n = int(input())
    arr = list(map(int, input().split()))
    root = buildtree(arr)
    # Do something with the tree here, like print its elements.
    levelordertraversal(root)