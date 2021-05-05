
def minDiffEle(arr, key):
    # checking the 0th the last element, to avoid the out of bounds error
    if key <= arr[0]:
        return arr[0]

    if key >= arr[-1]:
        return arr[-1]


    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first+last)//2

        if key == arr[mid]:
            return arr[mid]

        elif key > arr[mid]:
            first = mid + 1

        else:
            last = mid - 1


    # after the while loop ends, eles at first and last indices are 
    # the closest to key
    if(abs(key - arr[first]) < abs(key - arr[last])):
        return arr[first]
    else:
        return arr[last]


print(minDiffEle([4, 6, 10], 17))