class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LL:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value, end=" ")
            curr = curr.next
        print()

    def reverse(self):
        def reverse1(curr, prev):
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            return reverse1(next_node, curr)

        self.head = reverse1(curr=self.head, prev=None)

LL1 = LL()
LL1.append(1)
LL1.append(2)
LL1.append(3)
LL1.append(4)

LL1.print_list()
LL1.reverse()
LL1.print_list()