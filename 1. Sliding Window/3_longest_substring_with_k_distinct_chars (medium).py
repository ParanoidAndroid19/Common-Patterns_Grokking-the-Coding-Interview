# def longestSubstring(k, dstr):
#     windowStart = 0
#     dictChar = {}
#     maxSubstr = ""
    
#     for windowEnd in range(0, len(dstr)):
# 		  # recording the char frequency
#         dictChar[dstr[windowEnd]] = dictChar.get(dstr[windowEnd], 0) + 1
        
#         if(len(dictChar) <= k):
#             if(len(dstr[windowStart:windowEnd+1]) > len(maxSubstr)):
#                 maxSubstr = dstr[windowStart:windowEnd+1]
#             # print(dstr[windowStart:windowEnd+1])
#         else:
#             # removing or subtracting the frequency of char
#             if(dictChar.get(dstr[windowStart], 0) == 1):
#                 dictChar.pop(dstr[windowStart])
#             else:
#                 dictChar[dstr[windowStart]] = dictChar.get(dstr[windowStart], 0) - 1
# 			  # shrink the window
#             windowStart = windowStart + 1
        
#     return len(maxSubstr)

def longestSubstring(k, dstr):
    windowStart = 0
    dictChar = {}
    maxSubstr = ""
    
    for windowEnd in range(0, len(dstr)):
        # recording the char frequency
        dictChar[dstr[windowEnd]] = dictChar.get(dstr[windowEnd], 0) + 1
        
        while(len(dictChar) > k):
            # removing or subtracting the frequency of char
            if(dictChar.get(dstr[windowStart], 0) == 1):
                dictChar.pop(dstr[windowStart])
            else:
                dictChar[dstr[windowStart]] = dictChar.get(dstr[windowStart], 0) - 1
            
            # shrink the window
            windowStart = windowStart + 1
            
        # record the max length
        if(len(dstr[windowStart:windowEnd+1]) > len(maxSubstr)):
            maxSubstr = dstr[windowStart:windowEnd+1]
            # print(dstr[windowStart:windowEnd+1])
        
    return len(maxSubstr)
    

longestSubstring(3, "cbbebi")
