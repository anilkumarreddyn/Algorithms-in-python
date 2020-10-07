def countingSort(arr, exp1): 

	n = len(arr) 

	# The output array elements that will have sorted arr 
	output = [0] * (n) 

	
	count = [0] * (10) 

	
	for i in range(0, n): 
		index = (arr[i]/exp1) 
		count[int((index)%10)] += 1
	for i in range(1,10): 
		count[i] += count[i-1] 

	i = n-1
	while i>=0: 
		index = (arr[i]/exp1) 
		output[ count[ int((index)%10) ] - 1] = arr[i] 
		count[int((index)%10)] -= 1
		i -= 1


	i = 0
	for i in range(0,len(arr)): 
		arr[i] = output[i] 

def radixSort(arr):
	max1 = max(arr)

	exp = 1
	while max1/exp > 0:
		countingSort(arr,exp)
		exp *= 10

# Driver code to test above
arr = [ 70, 45, 75, 9, 82, 24, 2, 66]
radixSort(arr)

for i in range(len(arr)):
	print(arr[i]),
