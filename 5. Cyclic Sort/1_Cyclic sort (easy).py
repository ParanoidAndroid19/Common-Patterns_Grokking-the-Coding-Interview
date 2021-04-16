def cyclicSort(arr):
    i = 0
    
    while i < len(arr):
        # if the number is at correct index only then we move forward
        if(arr[i] == i+1):
            i = i+1
        else:
            val = arr[i]
            # swapping to get number at correct index
            arr[i], arr[val-1] = arr[val-1], arr[i]
    
    return arr
    

print(cyclicSort([1, 5, 6, 4, 3, 2]))