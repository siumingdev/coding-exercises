import math


def solve(s, arr):
    min_length = math.inf
    start = 0
    window_sum = 0

    for end in range(len(arr)):
        window_sum += arr[end]
        while window_sum >= s:
            min_length = min(min_length, end - start + 1)
            window_sum -= arr[start]
            start += 1
        
    return min_length


print(solve(7, [2, 1, 5, 2, 3, 2]))
print(solve(7, [2, 1, 5, 2, 8]))
print(solve(8, [3, 4, 1, 1, 6]))