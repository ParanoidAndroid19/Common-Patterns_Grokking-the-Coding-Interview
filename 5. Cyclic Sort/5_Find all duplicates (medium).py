def findAllDuplicate(arr):
    i = 0
    dups = set()
    
    while i < len(arr):
        # if number not in correct index
        if arr[i] != i + 1:
            val = arr[i]
            # if duplicate, then append
            if arr[i] == arr[val-1]:
                dups.add(arr[i])
                i = i + 1
            # swap
            else:
                arr[i], arr[val-1] = arr[val-1], arr[i]
        else:
            i = i + 1
            
    return list(dups)
    
print(findAllDuplicate([4,3,2,7,8,2,3,1]))