import time

def linear_search(arr, target):
    print("\n--- Linear Search ---")
    start = time.perf_counter()

    for i in range(len(arr)):
        if arr[i] == target:
            end = time.perf_counter()
            case_type = (
                "Best Case" if i == 0 else
                "Average Case" if i < len(arr) // 2 else
                "Worst Case"
            )
            print(f"Time Taken: {(end - start):.10f} seconds")
            print(f"Time Complexity Type: {case_type}")
            return i

    end = time.perf_counter()
    print(f"Time Taken: {(end - start):.10f} seconds")
    print("Time Complexity Type: Worst Case (Not Found)")
    return -1

def binary_search(arr, target):
    print("\n--- Binary Search ---")
    low, high = 0, len(arr) - 1
    start = time.perf_counter()
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            end = time.perf_counter()
            case_type = "Best Case" if steps == 1 else "Average/Worst Case"
            print(f"Time Taken: {(end - start):.10f} seconds")
            print(f"Time Complexity Type: {case_type}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    end = time.perf_counter()
    print(f"Time Taken: {(end - start):.10f} seconds")
    print("Time Complexity Type: Worst Case (Not Found)")
    return -1

def main():
    # Manual array input
    raw_input = input("Enter array elements (space-separated): ")
    arr = list(map(int, raw_input.strip().split()))
    target = int(input("Enter the element to search: "))

    print("\nMenu:\n1. Linear Search\n2. Binary Search")
    choice = int(input("Enter your choice (1 or 2): "))

    match choice:
        case 1:
            index = linear_search(arr, target)

        case 2:
            arr.sort()  # Binary search needs sorted array
            index = binary_search(arr, target)

        case _:
            print("Invalid choice")
            return

    if index != -1:
        print(f"Element {target} found at index {index}")
    else:
        print(f"Element {target} not found.")

if __name__ == "__main__":
    main()
