class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left, self.right = left, right


def has_path(root, S):
  if root is None:
    if S:
      return False
    else:
      return True

  return has_path(root.left, S - root.val) or has_path(root.right, S - root.val)


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

  print("Tree has path: ", has_path(root, 23))
  print("Tree has path: ", has_path(root, 16))