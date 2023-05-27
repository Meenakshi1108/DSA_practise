def heapify(arr,n,i):
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

def heapsort(arr):
	n=len(arr)
	lastnonleaf=(n//2)-1 

	for i in range(lastnonleaf, -1, -1):
	    heapify(arr, n, i)
	for i in range(n-1,0,-1):
		arr[i],arr[0]=arr[0],arr[i]
		heapify(arr,i,0)

	for i in range(n):
		print(arr[i],end=" ")
	print()
arr=list(map(int,input().split()))
heapsort(arr)