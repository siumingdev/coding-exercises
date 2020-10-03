from collections import deque


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left, self.right = left, right


def traverse(root):
  depth = 1
  Q = deque()
  Q.append(root)
  while Q:
    level_size = len(Q)
    for _ in range(level_size):
      node = Q.popleft()
      if node.left is not None:
        Q.append(node.left)
      if node.right is not None:
        Q.append(node.right)
      if node.left is None or node.right is None:
        return depth
      depth += 1

  return depth


if __name__ == "__main__":
  root = TreeNode(
    12,
    TreeNode(
      7,
      TreeNode(9)
    ),
    TreeNode(
      1,
      TreeNode(10),
      TreeNode(5)
    )
  )

  print("Tree Minimum Depth:", traverse(root))
