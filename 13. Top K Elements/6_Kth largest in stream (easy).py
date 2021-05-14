class kthLargestinStream:
    minHeap = []
    
    def __init__(self, nums, k):
        self.k = k
        
        for num in nums:
            self.add(num)
            
    def add(self, num):
        heappush(self.minHeap, num)
        
        # so that at a time only k elements are in minHeap and
        # num at root is the kth largest
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
            
        return self.minHeap[0]


kthLar = kthLargestinStream([3, 1, 5, 12, 2, 11], 4)
print(kthLar.add(-3))
print(kthLar.add(-2))
print(kthLar.add(-4))
print(kthLar.add(0))
print(kthLar.add(4))