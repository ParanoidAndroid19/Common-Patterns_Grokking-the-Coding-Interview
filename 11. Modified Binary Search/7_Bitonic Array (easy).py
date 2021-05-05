def bitonicArray(arr):
    first = 0
    last = len(arr) - 1
    
    while first < last:
        mid = (first+last)//2
        
        # greatest num should be before mid+1
        if arr[mid] > arr[mid+1]:
            last = mid
        
        # the greatest num should be after mid
        else:
            first = mid + 1

    # while loop ends when first == last, both the indices will be at
    # the greatest number in array 
    return arr[first]
    
    
print(bitonicArray([10, 9, 8]))