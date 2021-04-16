
def insert(intervals, new_interval):
    i = 0
    start = 0
    end = 1
    merged = []
    
    # directly appending all the intervals before new_interval to merged
    # since all i/p intervals are non overlapping
    # Skip all intervals which end before the start of the new interval
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i = i + 1
        
    # merging all intervals that overlap with new_interval
    # If current interval overlaps with the new interval 
    # (i.e. curr.start <= new_interval.end), we need to merge them into a new interval
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i = i + 1
        
    # appending this new_interval in merged
    merged.append(new_interval)
    
    # directly appending the rest of intervals
    while i < len(intervals):
        merged.append(intervals[i])
        i = i + 1
        
    return merged

    
    
print(insert([[1,3], [5,7], [8,12]], [4,6]))