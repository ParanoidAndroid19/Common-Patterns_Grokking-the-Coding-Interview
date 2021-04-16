def findMissingNums(arr):
    i = 0
    missing = []
    
    while i < len(arr):
        # num is not at correct position
        if arr[i] != i + 1:
            val = arr[i]
            # duplicates, ignore them
            if arr[i] == arr[val-1]:
                i = i + 1
            #swap
            else:
                arr[i], arr[val-1] = arr[val-1], arr[i]
        else:
            i = i + 1
            
    # after sorting
    for i in range(0, len(arr)):
        # whenever the number is not in correct position
        if(arr[i] != i + 1):
            missing.append(i+1)
            
    return missing
    
    
print(findMissingNums([2, 3, 1, 8, 2, 3, 5, 1]))