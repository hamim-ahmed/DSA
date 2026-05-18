def merge(arr, left, mid, right):

    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]

    i = 0
    j = 0
    k = left      #index for original array.

    # Merge two sorted parts
    while i < len(left_part) and j < len(right_part):

        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

        k += 1

    # Remaining left elements
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Remaining right elements
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def merge_sort_stack(arr):

    n = len(arr)

    stack = []

    # push initial range
    stack.append((0, n - 1, False))

    while stack:

        left, right, processed = stack.pop()

        if left >= right:
            continue

        mid = (left + right) // 2

        # If already processed, merge now
        if processed:
            merge(arr, left, mid, right)

        else:
            # Post-order simulation
            stack.append((left, right, True))

            stack.append((mid + 1, right, False))
            stack.append((left, mid, False))

    return arr


# Example
arr = [38, 27, 43, 3, 9, 82, 10]

print("Original:", arr)

merge_sort_stack(arr)

print("Sorted:", arr)