n,m = map(int,input().split())
s = []
d = dict()
for i in range(n):
	temp = input()
	s.append(temp)
	if temp not in d:
		d[temp] = 1
	else:
		d[temp]+=1
reslen = 0
s1 = []
s2 = []
res = []
for i in d:
	if d[i]!=0:
		temp = i[::-1]
		if i==temp:
			if d[i]==1:
				s1.append(i)
			else:
				for j in range(d[i]//2):
					s2.insert(0,i)
					s2.append(i)
					reslen+=2*m
				if d[i]%2!=0:
					s1.append(i)
		elif temp in d:
			co = min(d[i],d[temp])
			for j in range(co):
				s2.insert(0,i)
				s2.append(temp)
				reslen+=(2*m)
			d[temp] = 0
res+=s2[:len(s2)//2]
if s1:
	res+=s1[0]
	reslen+=m
res+=s2[len(s2)//2:]
print(reslen)
print("".join(res))
