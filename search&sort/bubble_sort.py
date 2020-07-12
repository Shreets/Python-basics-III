array = [2, 1, 4, 3, 5, 7]
arr_length = len(array)

for i in range(arr_length-1):
    if array[i] > array[i+1]:
        temp = array[i]
        array[i] = array[i+1]
        array[i+1] = temp

print(array)
