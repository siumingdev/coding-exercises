import time


def cyclic_sort(arr):
  i = 0
  while i < len(arr):
    if arr[i] == i + 1:
      i += 1
    else:
      a, b = arr[arr[i] - 1], arr[i]
      arr[i], arr[b - 1] = a, b
  return arr


if __name__ == '__main__':
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))