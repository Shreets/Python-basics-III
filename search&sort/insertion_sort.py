array = [7,2,4,1,5,3]
array_length = len(array)

for i in range(array_length):
    value = array[i]
    index = i
    while i > 0 and array[i - 1] > value:
        array[i] = array[i-1]
        i = i-1
    array[i] = value
print(array)

