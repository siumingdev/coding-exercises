class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left, self.right = left, right


def traverse(root):
  result = []
  def visit(value, level):
    while level >= len(result):
      result.append([])
    result[level].append(value)

  def _traverse(node, level):
    if node is not None:
      visit(node.val, level)
      _traverse(node.left, level + 1)
      _traverse(node.right, level + 1)
  
  _traverse(root, 0)
  return result


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

  print("Level order traversal:", traverse(root))
