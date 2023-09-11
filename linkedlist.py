class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def linked_list_del(self, key):
        current = self.head
        if current is not None:
            if current == key:
                self.head = current.next
                current = None
                return

        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next

        if current == None:
            return

        prev.next = current.next


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.linked_list_del(30)
linked_list.display()
