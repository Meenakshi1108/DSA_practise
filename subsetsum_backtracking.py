def findSubset(arr,k,i,sumc,remain):
	n=len(arr)
	if(i+1>n):
		return False
	if(sumc+remain<k):
		return False #undershooting

	nxt=arr[i+1]
	if(sumc+nxt==k):
		print(k,"=",nxt,end="")
		return True

	if(findSubset(arr,k,i+1,sumc+nxt,remain-nxt)):
		print("+",nxt,end="")
		return True
	else:
		return findSubset(arr,k,i+1,sumc,remain) #nxt not included


arr=[2,2,5,1,8,10]
r=sum(arr)
findSubset(arr,10,-1,0,r)
