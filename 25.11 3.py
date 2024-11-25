class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, position):
        if position < 1:
            print("False")
            return
        if position == 1:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        count = 1
        current = self.head
        while current and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Not stated")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_by_value(self, data):
        current = self.head
        previous = None
        if current is not None and current.data == data:
            self.head = current.next
            current = None
            return
        while current is not None and current.data != data:
            previous = current
            current = current.next
        if current is None:
            return
        previous.next = current.next
        current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def generate_sequence(self):
        sequence = []
        current = self.head
        while current:
            sequence.append(current.data)
            current = current.next
        return sequence


linked_list = LinkedList()


linked_list.insert_at_beginning(5)
linked_list.insert_at_beginning(3)
linked_list.insert_at_position(4, 2)


linked_list.print_list

