def find_missing_number(arr):
  for i in range(len(arr)):
    while i != arr[i] and arr[i] < len(arr):
      j = arr[i]
      arr[i], arr[j] = arr[j], arr[i]

  for i in range(len(arr)):
    if i != arr[i]:
      return i
      
  return len(arr)


if __name__ == '__main__':
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
