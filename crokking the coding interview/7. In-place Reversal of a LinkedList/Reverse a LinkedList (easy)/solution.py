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


def reverse(head):
  previous = None
  current = head
  while current is not None:
    next = current.next
    current.next = previous
    previous = current
    current = next  
  return previous


if __name__ == "__main__":
  head = Node(2, Node(4, Node(6, Node(8, Node(10)))))

  print("Nodes of original LinkedList are:", head)
  print("Nodes of reversed LinkedList are:", reverse(head))
