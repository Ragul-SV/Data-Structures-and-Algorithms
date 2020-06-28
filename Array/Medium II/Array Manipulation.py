n,qu = map(int,input().split())
arr = [0]*(n+1)
for q in range(qu):
	l,r,val = map(int,input().split())
	arr[l-1] += val
	if r!=n:
		arr[r] -= val
res = 0
temp = 0
for i in range(n):
	temp += arr[i]
	res = max(res,temp)
print(res)
