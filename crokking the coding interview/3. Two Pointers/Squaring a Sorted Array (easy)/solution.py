def make_squares(arr):
    squares = []

    pos_ptr = 0
    for i, x in enumerate(arr):
        if x > 0:
            pos_ptr = i
            break

    if pos_ptr == 0:
        return list(map(lambda x: x ** 2, squares))

    neg_ptr = pos_ptr - 1
    while neg_ptr >= 0 or pos_ptr < len(arr):
        if neg_ptr == 0:
            squares.append(arr[pos_ptr])
            pos_ptr += 1
        elif pos_ptr == len(arr) - 1:
            squares.append(arr[neg_ptr])
            neg_ptr -= 1
        else:
            if -arr[neg_ptr] < arr[pos_ptr]:
                squares.append(arr[neg_ptr] ** 2)
                neg_ptr -= 1
            else:
                squares.append(arr[pos_ptr] ** 2)
                pos_ptr += 1

    return squares


print(make_squares([-2, -1, 0, 2, 3]))
print(make_squares([-3, -1, 0, 1, 2]))
