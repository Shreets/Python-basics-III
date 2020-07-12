array_list = [4, 14, 16, 17, 19, 21, 24, 28, 30, 35, 36, 38, 39, 40, 41, 43]
array_len = len(array_list)


def interpolation(array, arr_length, item):
    low = 0
    high = arr_length-1

    while low <= high and array[low] <= item <= array[high]:
        if low == high:
            if array[low] == item:
                return f'the number {item} fround in index {low}'
            return 'number not found in the list'
        # pos = lo + [(x - arr[lo]) * (hi - lo) / (arr[hi] - arr[Lo])]
        pos = low + int(((item - array[low]) * float(high - low) / (array[high] - array[low])))

        if array[pos] == item:
            return f'the number {item} fround in index {pos}'

        if array[pos] < item:
            low = pos + 1
        else:
            high = pos - 1

    return 'number not found in the list'


print(interpolation(array_list, array_len, 39))
