def subSetsDups(nums):
    res = []
    res.append([])
    
    start = 0
    end = 0
    
    # sort the list so that dups check works
    nums.sort()
    
    for i in range(len(nums)):
        # reset start to 0 every time
        start = 0
        
        # check if current num is same as prev, thus duplicate
        # if it is then start as end (before end is updated)
        # this this end is the one before prev num's subsets are appended to res
        # this end is at the start of the prev num's subsets
        # if num is dup, then make subsets with only prev num's subsets
        if i > 0 and nums[i] == nums[i-1]:
            start = end
        
        # updating the end after appending all subsets for prev in last iteration
        end = len(res)
        
        # in case of dups, b/w start and end lies the prev num's subsets
        for j in range(start, end):
            newSub = list(res[j])
            newSub.append(nums[i])
            res.append(newSub)
            
    return res
    
    
print(subSetsDups([3, 1, 3]))