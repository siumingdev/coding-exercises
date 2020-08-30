def find_all_duplicates(arr):
  duplicates = set()
  i = 0
  while i < len(arr):
    j = arr[i] - 1
    if i != j:
      if arr[i] == arr[j]:
        duplicates.add(arr[i])
        i += 1
      else:
        arr[i], arr[j] = arr[j], arr[i]
    else:
      i += 1
  return list(duplicates)


if __name__ == '__main__':
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
