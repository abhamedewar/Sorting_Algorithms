def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min = i
        for j in range(i, n):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr


