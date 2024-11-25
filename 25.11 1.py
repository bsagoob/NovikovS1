class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

target_element = int(input("Введите элемент:"))

found = linked_list.search(target_element)

if found:
    print("true")
else:
    print("false")


