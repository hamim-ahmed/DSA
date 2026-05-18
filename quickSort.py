def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort_stack(arr):

    stack = []

    low = 0
    high = len(arr) - 1

    stack.append((low, high))

    while stack:

        low, high = stack.pop()

        if low < high:

            pi = partition(arr, low, high)    #sorting the  current sub and return the new sub index

            # Push right side
            stack.append((pi + 1, high))

            # Push left side
            stack.append((low, pi - 1))

    return arr


# Example
arr = [10, 7, 8, 9, 1, 5]

print("Original:", arr)

quick_sort_stack(arr)

print("Sorted:", arr)