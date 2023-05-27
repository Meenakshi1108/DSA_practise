# Question 9,10,15

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, k):
        self.heap.append(k)
        self.upheap(len(self.heap)-1)

    def getMin(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMin(self):
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.minheapify(0)
            return min
        elif len(self.heap) == 1:
            min = self.heap[0]
            del self.heap[0]
            return min
        else:
            return None

    def upheap(self, index):
        parent = (index-1)//2
        if index <= 0:
            return
        elif self.heap[parent] > self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.upheap(parent)

    def minheapify(self, index):
        smallest = index
        left = 2*index + 1
        right = 2*index + 2
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            tmp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = tmp
            self.minheapify(smallest)

bheap = BinaryHeap()
bheap.insert(20)
bheap.insert(10)
bheap.insert(30)
print(bheap.getMin())
bheap.removeMin()
print(bheap.getMin())