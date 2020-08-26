class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_cycle_length(head):
    # return -1 if no cycle
    slow_ptr = head
    fast_ptr = head
    while True:
        if fast_ptr is None:
            return -1
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            break

    current = slow_ptr
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow_ptr:
            break
    
    return cycle_length


def find_cycle_start(head):
    ptr1 = head
    ptr2 = head
    for _ in range(find_cycle_length(head)):
        ptr2 = ptr2.next

    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList has cycle: " + str(find_cycle_start(head).value))
