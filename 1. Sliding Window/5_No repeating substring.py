
def non_repeating_substring(dstr):
    windowStart = 0
    charIndexMap = {}
    longestSubstr = 0

    for windowEnd in range(0, len(dstr)):
        rightChar = dstr[windowEnd]

        if rightChar in charIndexMap:
            windowStart = max(windowStart, charIndexMap[rightChar] + 1)

        charIndexMap[rightChar] = windowEnd

        longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)

    return longestSubstr


non_repeating_substring("dvdgfgdf")