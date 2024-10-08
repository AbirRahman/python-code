def quick_sort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

array = [64, 25, 12, 22, 11]
quick_sort(array, 0, len(array) - 1)
print("Sorted array:", array)

--------------
// Output: Sorted array: [11, 12, 22, 25, 64]
