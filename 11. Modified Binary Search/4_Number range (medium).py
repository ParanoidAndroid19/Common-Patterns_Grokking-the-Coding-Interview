def findRange(arr, key):
    result = [-1, -1]
    # finding the first index of key
    result[0] = binSearch(arr, key, False)
    # if key exists and it's first occurance is found
    if result[0] != -1:
        # finding the last index of key
        result[1] = binSearch(arr, key, True)
    
    return result
    
    
def binSearch(arr, key, findMaxIndex):
    keyIndex = -1
    first = 0
    last = len(arr) - 1
    
    while first <= last:
        mid = (first+last)//2
        
        if key < arr[mid]:
            last = mid - 1
        
        elif key > arr[mid]:
            first = mid + 1
            
        else:
            keyIndex = mid
            if findMaxIndex:
                # search ahead to find the last index of key
                first = mid + 1
            else:
                # search behind to find the first index of key
                last = mid - 1
                
    return keyIndex
        

print(findRange([4, 6, 6, 6, 9], 6))
