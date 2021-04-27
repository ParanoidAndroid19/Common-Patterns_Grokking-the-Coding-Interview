from heapq import *

# -ve is used to implement a maxHeap, using -ve gives the required
# reverse properties of minHeap.

class MedianStream:
    def __init__(self):
        # containing first half of numbers
        # max no. at root
        self.maxHeap = []
        # containing second half of numbers
        # min no. at root
        self.minHeap = []
        

    def insertNum(self, num):
        # if maxHeap is empty or num is less than or equal to root
        # then push to max heap
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
            
        # either both heaps will have equal no. of elements or
        # maxHeap will have one more ele than minHeap
        # if not then balance both heaps
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
            
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
            
    
    def findMedian(self):
        # if steam of nums is even, take average of middle two ele
        # that is max from maxHeap and min from minHeap both at root
        if len(self.maxHeap) == len(self.minHeap):
            med = (-self.maxHeap[0] + self.minHeap[0]) / 2.0
            return med 
        
        # if not even, then since maxHeap has 1 more ele than minHeap
        # return root of maxHeap
        return -self.maxHeap[0]
        
    def printStream(self):
        print(self.maxHeap[::-1])
        print(self.minHeap)
        
        
stream = MedianStream()

stream.insertNum(3)
stream.insertNum(1)
stream.insertNum(5)
stream.insertNum(4)
print(stream.findMedian())
stream.printStream()
        
        