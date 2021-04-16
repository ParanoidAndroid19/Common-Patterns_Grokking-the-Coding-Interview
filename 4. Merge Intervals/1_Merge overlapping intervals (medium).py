class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end 
        

def merge(intervals):
    if(len(intervals) < 2):
        return intervals
        
    # converting them into Interval objects
    for i in range(0, len(intervals)):
            intervals[i] = Interval(intervals[i][0], intervals[i][1])
        
    # sort the intervals according to the start time
    intervals.sort(key=lambda x: x.start)
    
    # this start is the oldest, since intervals is sorted
    start = intervals[0].start
    end = intervals[0].end
    
    # final array of merged intervals
    mergeIntervals = []
    
    # starting from 1, since 0th interval is already being used
    for i in range(1, len(intervals)):
        interval = intervals[i]
        
        # interval.start definitely comes after start, since intervals is sorted
        # this means current interval's start lies b/w start and end
        # thus this is an overlapping interval
        if(interval.start <= end):
            # merging current overlapping interval by setting new end
            end = max(interval.end, end)
        
        else:
            # Since intervals is sorted, entering else means there are no more intervals to be merged with [start, end] interval
            # appending the [start, end] interval to the mergeIntervals
            mergeIntervals.append([start, end])
            # Updating start and end to the current interval, for future merging
            start = interval.start
            end = interval.end
            
    # appending the final [start, end] interval to mergeIntervals
    mergeIntervals.append([start, end])
    
    return mergeIntervals
    
    
print(merge([[1,3],[2,6],[8,10],[15,18]]))