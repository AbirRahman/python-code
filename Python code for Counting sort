def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for i in arr:
        count[i] += 1
    index = 0
    for i in range(max_value + 1):
        for j in range(count[i]):
            arr[index] = i
            index += 1
    return arr

arr = [64, 25, 12, 22, 11]
print("Sorted array:", counting_sort(arr))


// output: Sorted array: [11, 12, 22, 25, 64]
