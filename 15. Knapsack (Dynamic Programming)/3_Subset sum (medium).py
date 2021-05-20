
def findSubset(nums, ssum):
    memo = {}
    return recursive_subset(memo, nums, ssum, 0)
    

def recursive_subset(memo, nums, ssum, currentIndex):
    # success condition
    if ssum == 0:
        return True
        
    if currentIndex >= len(nums) or len(nums) == 0:
        return False
        
    if (currentIndex, ssum) not in memo:
        # including num at currentIndex
        if nums[currentIndex] <= ssum:
            if(recursive_subset(memo, nums, ssum - nums[currentIndex], currentIndex + 1)):
                memo[currentIndex, ssum] = True
                return True
                
        # excluding num at currentIndex
        memo[currentIndex, ssum] = recursive_subset(memo, nums, ssum, currentIndex + 1)
        
        
    return memo[currentIndex, ssum]
    
    
print(findSubset([1, 3, 4, 8], 10))