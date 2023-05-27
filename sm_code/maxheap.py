class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, k):
        self.heap.append(k)
        self.upheap(len(self.heap)-1)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.maxheapify(0)
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None

    def upheap(self, index):
        parent = (index-1)//2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.upheap(parent)

    def maxheapify(self, index):
        largest = index
        left = 2*index + 1
        right = 2*index + 2
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            tmp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = tmp
            self.maxheapify(largest)

bheap = BinaryHeap()
bheap.insert(20)
bheap.insert(10)
bheap.insert(30)
print(bheap.getMax())
bheap.removeMax()
print(bheap.getMax())