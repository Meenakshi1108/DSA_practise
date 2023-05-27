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

def deepest_left(root):
    if(root is None):
        return
    q=[]
    ans = None    
    q.append(root)
    while(q):
        root=q.pop(0)
        if(root.left is not None):
            q.append(root.left)
            ans=root.left
        if(root.right is not None):
            q.append(root.right)
    return ans


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = buildtree(arr)
    # Do something with the tree here, like print its elements.
    x=deepest_left(root)
    print(x.data)