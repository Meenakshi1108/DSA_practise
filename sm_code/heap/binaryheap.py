n=-1
def min_heapify(arr,n,i):
	smallest=i
	left=2*i+1
	right=2*i+2

	if left<n and arr[smallest]>arr[left]:
		smallest=left
	if right<n and arr[smallest]>arr[right]:
		smallest=right
	if smallest!=i:
		arr[smallest],arr[i]=arr[i],arr[smallest]
		min_heapify(arr,n,smallest)


def max_heapify(arr,n,i):
	largest=i
	left=2*i+1
	right=2*i+2

	if left<n and arr[largest]<arr[left]:
		largest=left
	if right<n and arr[largest]<arr[right]:
		largest=right

	if largest!=i:
		arr[largest],arr[i]=arr[i],arr[largest]
		heapify(arr,n,largest)


def insert(arr,node):
	global n
	i=n-1
	arr.append(node)
	while i>0:
		parent=(i-1)//2
		if arr[i]<=arr[parent]:
			break
		arr[i],arr[parent]=arr[parent],arr[i]
		i=parent



def deletenode(arr,node):
	global n
	lastelement=arr[n-1]

	arr[0]=lastelement
	n=n-1
	heapify(arr,n,0)

def buildheap(arr):
	global n
	lastnonleaf=(n//2)-1 

	for i in range(lastnonleaf, -1, -1):
	    heapify(arr, n, i)

def printheap(arr):
	n=len(arr)
	for i in range(n):
		print(arr[i],end=" ")
	print()


arr=list(map(int,input().split()))
buildheap(arr)
n=len(arr)
insert(arr,15)
printheap(arr)