def countingSort(arr,exp):
	n = len(arr)
	output = [0]*n
	count = [0]*10
	for i in range(n):
		temp = arr[i]//exp
		count[temp%10]+=1
	for i in range(1,10):
		count[i] += count[i-1]
	for i in range(n-1,-1,-1):
		temp = arr[i]//exp
		output[count[temp%10]-1] = arr[i]
		count[temp%10] -= 1
	for i in range(n):
		arr[i] = output[i]
		
def radix(arr):
	maxele = max(arr)
	exp = 1
	while maxele//exp>0:
		countingSort(arr,exp)
		exp*=10
	
arr = [802,54,2,24,52,87,97,34,63,43,53,1,85,25]
radix(arr)
print(arr)
