swaps = 0
comparisons = 0


def check_sorted(arr):
    flag = 0
    i = 1
    while i < len(arr):
        if arr[i].bike_path_length < arr[i - 1].bike_path_length:
            flag = 1
        i += 1
    if not flag:
        print("List is already sorted")
        return True
    else:
        return False


def bubble_sort(arr):
    global comparisons, swaps
    n = len(arr) - 1

    for j in range(n):
        for i in range(n):
            comparisons += 1
            if int(arr[i].bike_path_length) < int(arr[i + 1].bike_path_length):
                swaps += 1
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    print("Comparisons: ", comparisons, "\nSwaps: ", swaps)
    comparisons = 0
    swaps = 0


def quick_sort(arr):
    quick_sort2(arr, 0, len(arr)-1)
    print("Comparisons: ", comparisons, "\nSwaps: ", swaps)


def quick_sort2(arr, low, hi):
    if low < hi:
        p = partition(arr, low, hi)
        quick_sort2(arr, low, p-1)
        quick_sort2(arr, p+1, hi)


def get_pivot(arr, low, hi):
    mid = (hi + low)//2
    pivot = hi
    if int(arr[low].ticket_price) < int(arr[mid].ticket_price):
        if int(arr[mid].ticket_price) < int(arr[hi].ticket_price):
            pivot = mid
    elif int(arr[low].ticket_price) < int(arr[hi].ticket_price):
        pivot = low
    return pivot


def partition(arr, low, hi):
    global comparisons, swaps
    pivot_index = get_pivot(arr, low, hi)
    pivot_value = int(arr[pivot_index].ticket_price)
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    border = low

    for i in range(low, hi+1):
        comparisons += 1
        if int(arr[i].ticket_price) < pivot_value:
            swaps += 1
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[low], arr[border] = arr[border], arr[low]
    return border
