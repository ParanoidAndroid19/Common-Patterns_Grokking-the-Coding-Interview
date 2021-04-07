def fruitBasket(fruits):
    windowStart = 0
    longestSubarray = 0
    # minFreq = 10**5
    fruitTypes = {}
    # fruitNames = []
    
    for windowEnd in range(0, len(fruits)):
        fruitTypes[fruits[windowEnd]] = fruitTypes.get(fruits[windowEnd], 0) + 1
        
        while(len(fruitTypes) > 2):
            # remove the windowStart and move it forward
            if(fruitTypes.get(fruits[windowStart], 0) == 1):
                fruitTypes.pop(fruits[windowStart])
            else:
                fruitTypes[fruits[windowStart]] = fruitTypes.get(fruits[windowStart], 0) - 1
            
            windowStart = windowStart + 1
        
        # get fruit names
        # for fruit in fruitTypes:
        #     fruitNames.append(fruit)
        
        # record the longest subarray
        if((windowEnd - windowStart + 1) > longestSubarray):
            longestSubarray = windowEnd - windowStart + 1
            print(fruits[windowStart:windowEnd+1])
    
    print(longestSubarray)
            

fruitBasket([3,3,3,1,2,1,1,2,3,3,4])
            
            