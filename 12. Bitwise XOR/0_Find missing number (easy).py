def findMissingNum(arr):
    n = len(arr) + 1
    # xor sum of 1 to n (the nums that should be ideally present in array)
    x1 = 1
    for i in range(2, n+1):
        x1 = x1 ^ i
        
    # xor sum of all the numbers actually present in the array
    x2 = arr[0]
    for i in range(1, n-1):
        x2 = x2 ^ arr[i]
        
    # missing number is the xor of x1 and x2
    return x1 ^ x2
    
    
print(findMissingNum([1, 5, 2, 6, 4]))