t = int(input())
for cases in range(t):
	s = input()
	d = dict()
	flag = 1
	n = len(s)
	for i in range(n):
	    if s[i] not in d:
	        d[s[i]] = 1
	    else:
	        d[s[i]] += 1
	c = 0 
	for i in d.keys():
	    if d[i]%2!=0:
	        c+=1
	if (c==1 and n%2!=0) or (c==0 and n%2==0):
	    print("Yes")
	else:
	    print("No")
