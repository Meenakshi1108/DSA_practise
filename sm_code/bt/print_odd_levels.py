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

def print_odd(root,odd=True):
	if root is None:
		return None
	if(odd):
		print(root.data,end=" ")

	print_odd(root.left,not odd)
	print_odd(root.right,not odd)



t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = buildtree(arr)
    # Do something with the tree here, like print its elements.
    print_odd(root)