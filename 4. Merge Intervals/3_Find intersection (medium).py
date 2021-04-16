# def find_intersection(arr1, arr2):
#     res = []
#     start = 0
#     end = 1
#     i = 0
#     j = 0
    
#     while i < len(arr1) and j < len(arr2):
        
#         if len(arr1[i]) >= len(arr2[j]):
#             if(arr1[i][start] <= arr2[j][start] or arr1[i][end] >= arr2[j][end]):
#                 cstart = max(arr1[i][start], arr2[j][start])
#                 cend = min(arr1[i][end], arr2[j][end])
#                 res.append([cstart, cend])
#             j = j + 1
                
#         else:
#             if(arr2[j][start] <= arr1[i][start] or arr2[j][end] >= arr1[i][end]):
#                 cstart = max(arr1[i][start], arr2[j][start])
#                 cend = min(arr1[i][end], arr2[j][end])
#                 res.append([cstart, cend])
#             i = i + 1

#     while i < len(arr1):
#         res.append(arr1[i])
        
#     while j < len(arr2):
#         res.append(arr2[j])
        
        
#     return res


def find_intersection(arr1, arr2):
    res = []
    start = 0
    end = 1
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        
        # check if arr1[i] overlaps with arr2[j]
        # that is check if arr1[i]'s start lies in arr2[j] interval
        arr1_overlaps_arr2 = arr2[j][start] <= arr1[i][start] and arr1[i][start] <= arr2[j][end]

        # check if arr2[j] overlaps with arr1[i]
        # that is check if arr2[j]'s start lies in arr1[i] interval
        arr2_overlaps_arr1 = arr1[i][start] <= arr2[j][start] and arr2[j][start] <= arr1[i][end]
        
        # if either overlaps the other then
        if(arr1_overlaps_arr2 or arr2_overlaps_arr1):
            cstart = max(arr1[i][start], arr2[j][start])
            cend = min(arr1[i][end], arr2[j][end])
            res.append([cstart, cend])
            
        # move next from the interval which is finishing first
        if(arr1[i][end] < arr2[j][end]):
            i = i + 1
        else:
            j = j + 1
        
    return res


print(find_intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))