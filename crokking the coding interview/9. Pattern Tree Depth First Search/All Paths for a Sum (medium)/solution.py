class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left, self.right = left, right


def find_paths(root, S):
  all_paths = []
  def dfs(node, path, cur_sum):
    path.append(node.val)
    next_sum = cur_sum - node.val
    if (node.left is None) and (node.right is None):
      if next_sum is 0:
        all_paths.append([*path])
    else:
      if node.left is not None:
        dfs(node.left, path, next_sum)
      if node.right is not None:
        dfs(node.right, path, next_sum)
    del path[-1]
  dfs(root, [], S)
  return all_paths

if __name__ == "__main__":
  root = TreeNode(
    12,
    TreeNode(
      7,
      TreeNode(4)
    ),
    TreeNode(
      1,
      TreeNode(10),
      TreeNode(5)
    )
  )

  print("Tree has paths: ", find_paths(root, 23))
  print("Tree has paths: ", find_paths(root, 16))