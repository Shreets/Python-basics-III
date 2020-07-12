array_list = [4, 14, 16, 17, 19, 21, 24, 28, 30, 35, 36, 38, 39, 40, 41, 43]
array_len = len(array_list)


def linear_search(array, value):
    for i in range(array_len):
        if array[i] == value:
            return f'The number {value} is in index {i}'


search = linear_search(array_list, 39)
print(search)
