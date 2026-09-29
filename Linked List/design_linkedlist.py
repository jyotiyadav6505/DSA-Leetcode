
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):

        current = self.head
        count = 0

        while current is not None:

            if count == index:
                return current.val

            current = current.next
            count += 1

        return -1

    def addAtHead(self, val):

        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def addAtIndex(self, index, val):

        if index == 0:
            self.addAtHead(val)
            return

        current = self.head
        count = 0

        while current is not None and count < index - 1:
            current = current.next
            count += 1

        if current is None:
            return

        new_node = Node(val)

        new_node.next = current.next
        current.next = new_node

    def deleteAtIndex(self, index):

        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0

        while current.next is not None and count < index - 1:
            current = current.next
            count += 1

        if current.next is None:
            return

        current.next = current.next.next


        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)