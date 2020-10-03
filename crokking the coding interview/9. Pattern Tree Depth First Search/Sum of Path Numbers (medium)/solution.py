class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left, self.right = left, right


def find_sum_of_path_numbers(root):
  def dfs(node, path_number, path_numbers_sum):
    if node is None:
      return path_numbers_sum
    cur_path_number = path_number * 10 + node.val
    if (node.left is None) and (node.right is None):
      return path_numbers_sum + cur_path_number
    cur_path_numbers_sum = dfs(node.left, cur_path_number, path_numbers_sum)
    return dfs(node.right, cur_path_number, cur_path_numbers_sum)

  return dfs(root, 0, 0)

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

  print("Total Sum of Path Numbers: ", find_sum_of_path_numbers(root))
