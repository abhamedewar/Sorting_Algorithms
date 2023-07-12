def partition(arr, low, high):
    pivot = low

    i = low
    j = high
    while i < j:
        while arr[i] <= arr[pivot] and i < high:
            i += 1
        while arr[j] > arr[pivot] and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    
    return j


def quick_sort(arr, low, high):

    if low  < high:
        pivot= partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

    return arr    

