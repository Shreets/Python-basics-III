array_list = [4, 14, 16, 17, 19, 21, 24, 28, 30, 35, 36, 38, 39, 40, 41, 43]


def merge_sort(arr):
    arr_length = len(arr)

    if arr_length < 2:
        return arr

    midpoint = arr_length // 2
    left = merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])

    merged_arr = []

    left_index = 0
    right_index = 0

    while True:
        if left[left_index] <= right[right_index]:
            merged_arr.append(left[left_index])
            left_index += 1
        else:
            merged_arr.append(right[right_index])
            right_index += 1

        if left_index > len(left) - 1:
            merged_arr += right[right_index:]
            break

        if right_index > len(right) - 1:
            merged_arr += left[left_index:]
            break

    return merged_arr


print(merge_sort(array_list))