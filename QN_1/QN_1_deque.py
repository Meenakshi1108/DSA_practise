class DequeNode:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, num):
        new_node = DequeNode(num)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_front(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def push_back(self, num):
        new_node = DequeNode(num)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_back(self):
        if self.tail is not None:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

    def front(self):
        return self.head.data if self.head else None

    def back(self):
        return self.tail.data if self.tail else None

    def is_empty(self):
        return not self.head and not self.tail

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data, '->', end="")
            curr = curr.next
        print()

# Example usage:
deque = Deque()

deque.push_front(10)
deque.push_back(20)
deque.push_front(5)
deque.push_back(30)
deque.push_back(40)
deque.push_back(50)

print("Front:", deque.front())  # Output: 5
print("Back:", deque.back())    # Output: 20
deque.traverse()
deque.pop_front()
deque.pop_back()

print("Front after pop:", deque.front())  # Output: 10
print("Back after pop:", deque.back())    # Output: 10

deque.traverse()  # Output: 10 ->
