class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    _ = []
    temp = self
    while temp is not None:
      _.append(str(temp.value))
      temp = temp.next
    return "[" + ", ".join(_) + "]"


def reverse(head, k):
  def reverse_sublist(prev_tail):
    cur_head = head if prev_tail is None else prev_tail.next
    previous = None
    current = cur_head
    i = 0
    while i < k and current is not None:
      next = current.next
      current.next = previous
      previous = current
      current = next
      i += 1

    if prev_tail is not None:
      prev_tail.next = previous
    cur_head.next = current
    return previous, cur_head  # head and tail of the sub list

  ret_head, first_tail = reverse_sublist(None)
  prev_tail_ = first_tail
  j = 0
  while prev_tail_.next is not None:
    if j % 2:
      _, prev_tail_ = reverse_sublist(prev_tail_)
    else:
      for _ in range(k):
        prev_tail_ = prev_tail_.next
    j += 1
  
  return ret_head


if __name__ == "__main__":
  head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))

  print("Nodes of original LinkedList are:", head)  # [1, 2, 3, 4, 5, 6, 7, 8]
  print("Nodes of reversed LinkedList are:", reverse(head, 3))  # [3, 2, 1, 4, 5, 6, 8, 7]
