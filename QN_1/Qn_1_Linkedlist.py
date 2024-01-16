class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, num):
        new_node = Node(num)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_from_start(self):
        if self.head is not None:
            self.head = self.head.next

    def insert_at_end(self, num):
        new_node = Node(num)
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def remove_from_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        curr = self.head
        prev = None
        while curr.next is not None:
            prev = curr
            curr = curr.next

        prev.next = None

    def front(self):
        return self.head

    def last(self):
        if self.head is None:
            return None

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data, '->', end="")
            curr = curr.next

    def reverse(self):
    	if(self.head.next is None or self.head is None):
    		return self.head

    	prev=None
    	temp=self.head

    	while(temp is not None):
    		front=temp.next
    		temp.next=prev
    		prev=temp 
    		temp=front

    	self.head=prev
    	return



my_linked_list = LinkedList()
my_linked_list.insert_at_start(3)
my_linked_list.insert_at_start(2)
my_linked_list.insert_at_start(1)

print("insertions at the start:")
my_linked_list.traverse()

my_linked_list.remove_from_start()

print("\nremoval from the start:")
my_linked_list.traverse()

my_linked_list.insert_at_end(4)
my_linked_list.insert_at_end(5)

print("\ninsertions at the end:")
my_linked_list.traverse()

my_linked_list.remove_from_end()

print("\nremoval from the end:")
my_linked_list.traverse()

first_element = my_linked_list.front().data
last_element = my_linked_list.last().data

print("\nFirst Element:", first_element)
print("Last Element:", last_element)


reverse=my_linked_list.reverse()
print("Reverse")
my_linked_list.traverse()
