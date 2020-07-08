import math


def solve(s, arr):
    n = len(arr)
    min_length = math.inf

    start = 0
    end = 0

    window_sum = 0

    while end <= n:
        # print(f'start: {start}, end: {end}, subarr: {arr[start:end]}')
        if window_sum < s:
            if end >= n:
                break
            window_sum += arr[end]
            end += 1
        elif window_sum >= s:
            min_length = min(min_length, end - start)
            window_sum -= arr[start]
            start += 1

    return min_length


print(solve(7, [2, 1, 5, 2, 3, 2]))
print(solve(7, [2, 1, 5, 2, 8]))
print(solve(8, [3, 4, 1, 1, 6]))