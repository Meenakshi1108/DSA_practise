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

def spiral_order_Rec(root):
    h=height(root)
    for i in range(1,h+1):
        printlevel(root,i,i%2)


def printlevel(root,level,flag):
    if root==None:
        return 
    if (level==1):
        print(root.data,end=" ")
    elif(level>1):
        if(flag==0):
            printlevel(root.right,level-1,flag)
            printlevel(root.left,level-1,flag)
        else:
            printlevel(root.left,level-1,flag)
            printlevel(root.right,level-1,flag)




def height(root):
    if root==None:
        return 0;
    else:
        left_height=height(root.left)
        right_height=height(root.right)

    return max(left_height,right_height)+1

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = buildtree(arr)
    # Do something with the tree here, like print its elements.
    spiral_order_Rec(root)
    print()