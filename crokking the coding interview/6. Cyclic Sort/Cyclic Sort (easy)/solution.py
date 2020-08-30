def cyclic_sort(arr):
  for i in range(len(arr)):
    while i != arr[i] - 1:
      j = arr[i] - 1
      arr[i], arr[j] = arr[j], arr[i]
      
  return arr


if __name__ == '__main__':
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))