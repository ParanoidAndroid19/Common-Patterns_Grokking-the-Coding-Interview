# return false if conflict

def check_conflict(intervals):
    start = 0
    end = 1
    
    intervals.sort(key = lambda x: x[start])
    
    for i in range(1, len(intervals)):
        # check if overlaps
        if(intervals[i][start] < intervals[i-1][end]):
            return False
            
    return True
    
    
print(check_conflict([[4,5], [2,3], [3,6]]))