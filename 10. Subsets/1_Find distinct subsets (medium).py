def distinctSubsets(nums):
    res = []
    res.append([])
    
    for num in nums:
        for i in range(len(res)):
            newSub = list(res[i])
            newSub.append(num)
            res.append(newSub)
            
    return res
    
    
    
print(distinctSubsets([1, 3]))