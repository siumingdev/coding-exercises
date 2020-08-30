def find_missing_numbers(arr):
  for i in range(len(arr)):
    while i != arr[i] - 1 and arr[i] != arr[arr[i] - 1]:
      j = arr[i] - 1
      arr[i], arr[j] = arr[j], arr[i]
  
  missing_numbers = []
  for i in range(len(arr)):
    if i != arr[i] - 1:
      missing_numbers.append(i + 1)
      
  return missing_numbers


if __name__ == '__main__':
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))
