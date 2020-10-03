class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left, self.right = left, right


def find_path(root, sequence):
  if root is None:
    return len(sequence) == 0

  def dfs(node, sequence_idx):
    if node is None:
      return sequence_idx >= len(sequence)
    
    if node.val != sequence[sequence_idx]:
      return False

    return dfs(node.left, sequence_idx + 1) or dfs(node.right, sequence_idx + 1)

  return dfs(root, 0)

if __name__ == "__main__":
  root = TreeNode(
    1,
    TreeNode(
      0,
      TreeNode(1)
    ),
    TreeNode(
      1,
      TreeNode(6),
      TreeNode(5)
    )
  )

  print("Tree has path sequence: ", find_path(root, [1, 0, 7]))
  print("Tree has path sequence: ", find_path(root, [1, 1, 6]))
