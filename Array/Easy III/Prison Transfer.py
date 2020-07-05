n,t,c = map(int,input().split())
arr = list(map(int,input().strip().split()))
i =0 
k = 0
res = 0
while i<n:
	if arr[i]<=t:
		k+=1
	else:
		k=0
	if k>=c:
		res+=1
	i+=1
print(res)
