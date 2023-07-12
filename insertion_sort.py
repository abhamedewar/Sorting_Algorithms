def insertion_sort(arr):
    n = len(arr)
    for i in range(n):

        j = i
        
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr
