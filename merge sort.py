"""
Objective -
    1) Accept input of N elements
    2) Breakdown input into smaller arrays of 2 or 1 elements
    3) Combine results of all broken down elements and return a N element sorted list
Notes:
    Breaking down results in an ordered list which are sorted in it's scope
        When combining you can have 2 arrays in left [ -5, 100] and right [ 1, 2]
    -Need to iterate over all elements of both lists to get a comnined sorted list
"""
def sort(array) -> list:
    """
    Take an input of unsorted array.
    check if array is of a single element, if so return that.
    check if array is of 2 elements, sort those 2 elements and return them
    otherwise use iteration to go over array elements and sort it to main portion using merge sort.
    Refer to this video to understand merge sort- https://www.youtube.com/watch?v=mB5HXBb_HY8
    :param array: a list of n elements that are not sorted
    :return: a list of n elements that are sorted
    """
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
