def solve(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        cur_sum = arr[start] + arr[end]
        if cur_sum > target:
            end -= 1
        elif cur_sum < target:
            start += 1
        else:
            return [start, end]
    
    return [-1, -1]

print(solve([1, 2, 3, 4, 6], 6))
print(solve([2, 5, 9, 11], 11))