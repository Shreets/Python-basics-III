array = [7, 2, 1, 6, 8, 5, 3, 4]
arr_length = len(array)

start = 0


def partition(array, start, end):
    pivot = array[end]
    for i in range(start, end):
        if array[i] <= pivot:
            temp = array[i]
            array[i] = array[start]
            array[start] = temp
            start = start+1
    temp = array[start]
    array[start] = array[end]
    array[end] = temp
    return start


def quick_sort(array, start, end):
    if start < end:
        pos = partition(array, start, end)
        # print('pos : ',pos)
        quick_sort(array, start, pos - 1)
        quick_sort(array, pos + 1, end)


quick_sort(array, start, arr_length-1)
print(array)
