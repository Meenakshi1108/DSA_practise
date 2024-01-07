def subsetsum(arr,i,target):
	if(target==0):
		return True
	if(i==0):
		return arr[0]==target

	not_take=subsetsum(arr,i-1,target)
	take=float('inf')
	if(arr[i]<=target):
		take=subsetsum(arr,i-1,target-arr[i])

	return (take or not_take)


def subsetsumtab(arr,i,k):
	dp=[[False for i in range(k+1)]for i in range(n)]

	for i in range(n):
		dp[i][0]=True #empty sum



	if(arr[0]<=k):
		dp[0][arr[0]]=True
		#0th element can make up the target

	for i in range(1,n):
		for j in range(1,k+1):
			nottake=dp[i-1][k]
			take=float('-inf')
			if(arr[i]<=k):
				take=dp[i-1][k-arr[i]]

			dp[i][j]=nottake or take 

	return dp[n-1][k]





arr=[2,2,5,1,8,10]
n=len(arr)
print(subsetsum(arr ,n-1 , 10))
print(subsetsumtab(arr,n-1,10))
