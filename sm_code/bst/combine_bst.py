class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_bst(root, key):
    if root is None:
        root = Node(key)
        return root
    else:
        if key < root.data:
            root.left = insert_bst(root.left, key)
        else:
            root.right = insert_bst(root.right, key)
    return root


def inorder(root, arr):
    if root is None:
        return
    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)


def combine_bst(root1, root2):
    arr1 = []
    arr2 = []
    inorder(root1, arr1)
    inorder(root2, arr2)
    for i in arr2:
        arr1.append(i)
    arr1.sort()
    return arr1


t = int(input())
for i in range(t):
    arr2 = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))

    root1 = root2 = None
    for key in arr1:
        if key != -1:
            root1 = insert_bst(root1, key)
    for key in arr2:
        if key != -1:
            root2 = insert_bst(root2, key)
    arrcombined=combine_bst(root1, root2)
    root=arrcombined[len(arrcombined)//2]
    print("Root is ",root)
    print("combined bst is",*arrcombined)

    