import concurrent.futures
import random

def quicksort(arr):
    ##Todo
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        left_future = executor.submit(quicksort, left)
        right_future = executor.submit(quicksort, right)

        sorted_left = left_future.result()  # waits, and re-raises any thread error
        sorted_right = right_future.result()

    return sorted_left + middle + sorted_right

# Example usage:
arr = random.sample(range(1, 100), 20)
print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)