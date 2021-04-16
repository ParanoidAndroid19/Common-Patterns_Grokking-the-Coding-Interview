# My solution

def findMissingNum(arr):
    i = 0
    n = len(arr)
    
    # if n doesn't exist then it's the missing number
    missing = n
    
    while i < len(arr):
        # if the number is at correct index, then move i forward
        if(arr[i] == i):
            i = i + 1
        # if number is n then ignore it, as it's index falls out of array
        # if n exists, then after sorting it will be in place of the missing number,
        # hence the missing number is the index of n.
        # So keep recording the index of n for missing number
        elif(arr[i] == n):
            missing = i
            i = i + 1
        # swapping to get number in it's correct index
        else:
            val = arr[i]
            arr[i], arr[val] = arr[val], arr[i]
    
    return missing
    

print(findMissingNum([9,6,4,2,3,5,7,0,1]))