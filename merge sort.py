array = [887, 0, -48, -44]


def sort(array) -> list:
    #  print(f'Starting with {array=}')

    if len(array) < 2:
        #  print(f'\tArray has less than 2 elements. {array=}')
        return array
    elif len(array) == 2:
        a = [array[0], array[1]] if array[0] < array[1] else [array[1], array[0]]
        #  print(f'\tArray has 2 elements. {array=}. returning {a=}')
        return a

    # split
    mid_point = len(array) // 2
    left_array = sort(array[:mid_point])
    right_array = sort(array[mid_point:])

    # merge
    l = 0
    r = 0
    total = 0
    #  print(f'Elements before loop \n\t{array=}\n\t{left_array=}\n\t{right_array=}')
    while l < len(left_array) and r < len(right_array):
        #  print(f'Elements in loop{total=} \n\t{array=}\n\t{left_array=}\n\t{right_array=}')

        if left_array[l] < right_array[r]:
            # #  print(f'left array element "{left_array[l]}" is smaller than right element "{right_array[r]}"')
            array[total] = left_array[l]
            l += 1

        elif right_array[r] < left_array[l]:
            # #  print(f'right array element "{right_array[r]}" is smaller than left element "{left_array[l]}"')
            array[total] = right_array[r]
            r += 1

        else:
            # #  print(f'right array element "{right_array[r]}" is same as left element "{left_array[l]}"')
            array[total] = right_array[r]
            r += 1

        total += 1

    #  print(f'Elements after loop \n\t{array=}\n\t{left_array=}\n\t{right_array=}')
    if l < len(left_array):
        array[total:] = left_array[l:]
    if r < len(right_array):
        array[total:] = right_array[r:]
    #  print(f'returning {array=}')
    return array


print(sort([10, 1, 100, 2, 1, -88, 2]))
print(sort([10, 1, 100,  1, -88, 2]))
