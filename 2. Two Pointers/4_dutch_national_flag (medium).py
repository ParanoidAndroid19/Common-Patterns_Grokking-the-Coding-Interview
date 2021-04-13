
def sortColors(arr):
    if(len(arr) == 1):
        return arr
    
    low = 0
    high = len(arr) - 1
    i = 0
    
    # <= high so that even the num at high is looked at
    while i <= high:
        # all 0 should be before low
        if(arr[i] == 0):
            # swap with low
            arr[i], arr[low] = arr[low], arr[i]
            # increment both low and i, because we know for sure that low and i both are 0
            i = i + 1
            low = low + 1
        # all 1 should be b/w low and high
        elif(arr[i] == 1):
            i = i + 1
        # all 2 should be after high
        else:
            # swap with high
            arr[i], arr[high] = arr[high], arr[i]
            # decrement only high
            high = high - 1
            # don't increment i, since we don't know what came in place of i after swiping with high, it could be 0, 1 or 2
    
    return arr