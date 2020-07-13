def dutch_flag_sort(a):
    l, m, r = 0, 0, len(a) - 1
    while (m <= r):
        if a[m] == 0:
            a[m], a[l] = a[l], a[m]
            m += 1
            l += 1
        elif a[m] == 2:
            a[m], a[r] = a[r], a[m]
            r -= 1
        else:
            m += 1

    return a


print(dutch_flag_sort([1, 0, 2, 1, 0]))
print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))