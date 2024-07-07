
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

    def merge_two_lists(self, ll1, ll2):
        if not ll1:
            return ll2
        if not ll2:
            return ll1
        
        if ll1.value < ll2.value:
            ll1.next = self.merge_two_lists(ll1.next, ll2)
            return ll1
        else:
            ll2.next = self.merge_two_lists(ll1, ll2.next)
            return ll2

ll1 = LL()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LL()
ll2.append(2)
ll2.append(4)
ll2.append(6)

ll1.print_list()
ll2.print_list()

merged_list = LL()
merged_list.head = merged_list.merge_two_lists(ll1.head, ll2.head)
merged_list.print_list()
