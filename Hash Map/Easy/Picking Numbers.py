n = int(input())
arr = list(map(int,input().strip().split()))
d = dict()
for i in range(n):
	if arr[i] in d:
		d[arr[i]] += 1
	else:
		d[arr[i]] = 1
res = 0
for key,value in d.items():
	if key+1 in d:
		res = max(res,d[key]+d[key+1])
	else:
		res = max(res,d[key])
print(res)
