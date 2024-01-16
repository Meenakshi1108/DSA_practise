class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MaxHeap:
    def __init__(self):
        self.root = None
        self.heap = []

    def heapify_top_down(self, i):
        n = len(self.heap)
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.heap[largest].data < self.heap[left].data:
            largest = left
        if right < n and self.heap[largest].data < self.heap[right].data:
            largest = right
        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.heapify_top_down(largest)

    def heapify_bottom_up(self, i):
        parent = (i - 1) // 2
        if parent < 0:
            return
        elif self.heap[parent].data < self.heap[i].data:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.heapify_bottom_up(parent)

    def add(self, num):
        new_node = Node(num)
        self.heap.append(new_node)
        self.heapify_bottom_up(len(self.heap) - 1)

    def remove_max(self):
        if not self.heap:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop(0).data
        else:
            max_value = self.heap[0].data
            self.heap[0] = self.heap.pop()
            self.heapify_top_down(0)
            return max_value

    def max(self):
        return self.heap[0].data if self.heap else None

        
max_heap = MaxHeap()

# Add elements to the heap
max_heap.add(10)
max_heap.add(20)
max_heap.add(15)
max_heap.add(5)
max_heap.add(25)

print("Max Element:", max_heap.max())  # Output: 25

print("Removed Max Element:", max_heap.remove_max())  # Output: 25

print("Updated Max Element:", max_heap.max())  # Output: 20
