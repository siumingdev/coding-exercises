import math


def triplet_sum_close_to_target(arr, target):
    arr.sort()
    min_sum = math.inf
    min_diff = math.inf

    for i_a, a in enumerate(arr):
        i_b, i_c = i_a + 1, len(arr) - 1
        while i_b < i_c:
            b, c = arr[i_b], arr[i_c]
            cur_sum = a + b + c
            cur_diff = abs(cur_sum - target)
            if cur_diff < min_diff or (cur_diff == min_diff and cur_sum < min_sum):
                min_sum, min_diff = cur_sum, cur_diff
            if cur_sum > target:
                i_c -= 1
            elif cur_sum < target:
                i_b += 1
            else: # cur_sum == target, shortcut to return
                return min_sum

    return min_sum


print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
