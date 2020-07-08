n = int(input())
arr = list(map(int,input().strip().split()))
qu = int(input())
arr.sort()
s = [-1]*(arr[n-1]+1)
k = 0
s[0] = 0
for i in range(1,arr[n-1]+1):
	if i<arr[k]:
		s[i] = s[i-1]
	else:
		s[i] = s[i-1]
		while k<n and i>=arr[k]:
			s[i]+=1
			k+=1
for i in range(qu):
	q = int(input())
	if q<arr[n-1]:
		print(s[q])
	else:
		print(s[arr[n-1]])
