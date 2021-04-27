class MinHeap:
    def __init__(self):
        self.heapList = []
    
    def parentIndex(self, index):
        if index == 0:
            return 0
        return abs(index - 2)//2
        
    def leftIndex(self, index):
        return (index*2) + 1
        
    def rightIndex(self, index):
        return (index*2) + 2
        
    def hasParent(self, index):
        return self.parentIndex(index) >= 0
        
    def hasLeft(self, index):
        return self.leftIndex(index) < len(self.heapList)
        
    def hasRight(self, index):
        return self.rightIndex(index) < len(self.heapList)
        
    def parent(self, index):
        return self.heapList[self.parentIndex(index)]
        
    def leftChild(self, index):
        return self.heapList[self.leftIndex(index)]
        
    def rightChild(self, index):
        return self.heapList[self.rightIndex(index)]
        
        
    def heapifyUp(self):
        # bubble up the element at leaf upwards
        index = len(self.heapList) - 1
        while(self.hasParent(index) and self.parent(index) > self.heapList[index]):
            # swap
            self.heapList[self.parentIndex(index)], self.heapList[index] = self.heapList[index], self.heapList[self.parentIndex(index)]
            index = self.parentIndex(index)

    def add(self, item):
        self.heapList.append(item)
        self.heapifyUp()
        
        
    def heapifyDown(self):
        # bubble down the largest ele at root to leaf
        index = 0
        
        # only check for left, since if there is no left child, there also won't be no right child
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftIndex(index)
            if(self.hasRight(index)):
                if(self.rightChild(index) < self.leftChild(index)):
                    smallerChildIndex = self.rightIndex(index)
                    
            if(self.heapList[index] < self.heapList[smallerChildIndex]):
                break
            else:
                # swap
                self.heapList[smallerChildIndex], self.heapList[index] = self.heapList[index], self.heapList[smallerChildIndex]
                
            index = smallerChildIndex

        
    def getMin(self):
        lenHeap = len(self.heapList)
        
        if lenHeap == 0:
            return None
        
        minItem = self.heapList[0]
        # last ele of heap is now at root
        self.heapList[0] = self.heapList[-1]
        del self.heapList[-1]
        self.heapifyDown()
        
        return minItem
        
        
    def printHeap(self):
        print(self.heapList)
        
        
        
        
egHeap = MinHeap()

egHeap.add(10)
egHeap.add(15)
egHeap.add(20)
egHeap.add(17)

# add
# egHeap.printHeap()
# egHeap.add(8)
# egHeap.printHeap()

# get the min element
egHeap.add(25)
egHeap.printHeap()
print(egHeap.getMin())
egHeap.printHeap()
