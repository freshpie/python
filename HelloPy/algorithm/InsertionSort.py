arr = [4,1,5,2,1,1,7,8]

print(arr)
for i in range(1, len(arr)):
    key = arr[i]
    
    j = i-1
    while j>=0 and arr[j] > key:        
        arr[j+1] = arr[j]
        j=j-1
        #arr[j+1] = key
        #print(arr)
    arr[j+1] = key    
        
    
    print(arr)
    
    
    
