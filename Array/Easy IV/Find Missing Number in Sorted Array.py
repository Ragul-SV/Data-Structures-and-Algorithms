def binarysearch(arr,n):
	l=0
	h=n-1
	while l<h:
		mid=(l+h)//2
		if (arr[mid]-mid)!=arr[0]:
			if (arr[mid]-arr[mid-1])>1:
				return arr[mid]-1
			else:
				h=mid-1
		else:
			if (arr[mid+1]-arr[mid])>1:
				return arr[mid]+1
			else:
				l = mid+1
	return -1
	
arr = [7,8,9,10,11,12,13,14]
n = len(arr)
print(binarysearch(arr,n))
