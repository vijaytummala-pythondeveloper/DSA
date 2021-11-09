class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head  # moving cursor of LinkedList to tail
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def to_list(self):
        vals = []
        node = self.head
        while node:
            vals.append(node.val)
            node = node.next
        return vals


linkedList = LinkedList()
linkedList.append(10)
linkedList.append(20)
linkedList.append(30)
print(linkedList.to_list())
