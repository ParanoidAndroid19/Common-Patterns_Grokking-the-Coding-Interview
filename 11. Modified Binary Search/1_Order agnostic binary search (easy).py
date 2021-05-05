def orderAgnoBinSearch(arr, key):
    first = 0
    last = len(arr) - 1
    # check if array is sorted in ascending or descending order
    isAsce = arr[0] <= arr[-1]
    
    while first <= last:
        mid = (first+last)//2
        
        if arr[mid] == key:
            return mid
            
        else:
            if isAsce:
                if key < arr[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:
                if key < arr[mid]:
                    first = mid + 1
                else:
                    last = mid - 1
                    
    return -1

print(orderAgnoBinSearch([4, 6, 10], 10))