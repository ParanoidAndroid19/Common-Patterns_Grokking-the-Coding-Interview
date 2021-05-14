from heapq import *

def connectRope(minHeap):
    res = 0
    heapify(minHeap)

    while len(minHeap) > 1:
        temp = heappop(minHeap) + heappop(minHeap)
        res = res + temp
        heappush(minHeap, temp)

    return res


print(connectRope([1,8,3,5]))