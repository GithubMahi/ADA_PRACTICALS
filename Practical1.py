def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:l + n1]
    R = arr[m + 1:m + 1 + n2]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

def print_array(arr):
    print(" ".join(map(str, arr)))

n = int(input("Enter number of elements: "))
arr = [int(input("Enter element: ")) for _ in range(n)]

print("\n1. Bubble Sort\n2. Selection Sort\n3. Quick Sort\n4. Insertion Sort\n5. Merge Sort\n6. Exit")
choice = int(input("Choose sorting algorithm: "))

print("\nUnsorted array:", end=" ")
print_array(arr)

match choice:
    case 1:
        bubble_sort(arr)
    case 2:
        selection_sort(arr)
    case 3:
        quick_sort(arr, 0, n - 1)
    case 4:
        insertion_sort(arr)
    case 5:
        merge_sort(arr, 0, n - 1)
    case 6:
        exit()
    case _:
        print("Invalid choice")

print("Sorted array:", end=" ")
print_array(arr)
