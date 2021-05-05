import math

# array reader to get the value at index in array of unknown size
class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf

        return self.arr[index]


def searchInfArray(reader, key):
    # initial bounds is 2, then increase it exponentially
    start = 0
    end = 1

    # while key is out of the current bounds
    # key is greater than num at end index
    while reader.get(end) < key:
        # since key is greater than num at index end, new bounds start after it
        newStart = end + 1
        # we are doubling the bounds size (end-start+1)
        end = end + (end-start+1)*2
        start = newStart

    # out of the while loop means that either
    # key exists and is inside the bounds, before or at end index
    # key doesn't exist and index is out of bounds of the array
    return binSearch(reader, start, end, key)


def binSearch(reader, first, last, key):
    while first <= last:
        mid = (first+last)//2

        if key == reader.get(mid):
            return mid

        elif key > reader.get(mid):
            first = mid + 1

        else:
            last = mid - 1

    return -1


reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
print(searchInfArray(reader, 16))