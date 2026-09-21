
def maximum(arr, k):
    # Create a min-heap from the first k elements of the array
    heap = arr[:k]
    heapq.heapify(heap)

    # Iterate over the remaining elements of the array
    for num in arr[k:]:
        # If the current number is greater than the smallest number in the heap
        if num > heap[0]:
            # Replace the smallest number in the heap with the current number
            heapq.heapreplace(heap, num)

    # The heap now contains the k largest numbers in the array, so sort it and return it
    return sorted(heap)
