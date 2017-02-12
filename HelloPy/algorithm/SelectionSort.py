
def sort(arr, index):
	startIndex = len(arr)-index
	if startIndex < len(arr):
		#index : 배열의 시작 인덱스
		minNum = min(arr[startIndex:])
		minIndex = arr.index(minNum)
		
		temp = arr[startIndex] 		#시작인덱스의 값
		arr[startIndex] = minNum
		arr[minIndex] = temp
		
		sort(arr, index -1)
	
	return arr;

arr2 = [5,2,4,1,3,6]
print(arr2)

print(sort(arr2, len(arr2)))
		
