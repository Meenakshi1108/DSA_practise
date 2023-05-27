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

def buildheap(arr):
	n=len(arr)
	lastnonleaf=n//2 -1
	for i in range(lastnonleaf,-1,-1):
		min_heapify(arr,n,i)
	for i in range(n):
		print(arr[i],end=" ")
	print()


arr=list(map(int,input().split()))
buildheap(arr)


