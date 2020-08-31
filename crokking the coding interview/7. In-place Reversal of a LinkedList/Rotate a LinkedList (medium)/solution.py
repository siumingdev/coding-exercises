class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    _ = []
    temp = self
    max_length = 20
    while max_length and temp is not None:
      _.append(str(temp.value))
      temp = temp.next
      max_length -= 1
    if not max_length:
      _.append('...')
    return "[" + ", ".join(_) + "]"


def rotate(head, k):
  length = 0
  current = head
  while current is not None:
    current = current.next
    length += 1

  k = length - k % length
  new_head = head
  while k:
    new_head = head if new_head.next is None else new_head.next
    k -= 1
  
  current = new_head
  while True:
    if current.next is new_head:
      current.next = None
      break
    elif current.next is None:
      current.next = head
    current = current.next

  return new_head


if __name__ == "__main__":
  head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))

  print("Nodes of original LinkedList are:", head)  # [1, 2, 3, 4, 5, 6, 7, 8]
  print("Nodes of reversed LinkedList are:", rotate(head, 3))  # [4, 5, 6, 7, 8, 1, 2, 3]
