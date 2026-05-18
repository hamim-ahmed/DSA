def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort_stack(arr):

    # Stack for splitting
    split_stack = [arr]

    # Stack for sorted pieces
    sorted_stack = []

    # SPLITTING PHASE
    while split_stack:

        current = split_stack.pop()

        if len(current) <= 1:
            sorted_stack.append(current)

        else:

            mid = len(current) // 2

            left = current[:mid]
            right = current[mid:]

            # Push right first
            split_stack.append(right)

            # Push left second
            split_stack.append(left)

    # MERGING PHASE
    while len(sorted_stack) > 1:

        left = sorted_stack.pop(0)
        right = sorted_stack.pop(0)

        merged = merge(left, right)

        sorted_stack.append(merged)

    return sorted_stack[0]


# Example
arr = [38, 27, 43, 3, 9, 82, 10]

print("Original:", arr)

sorted_arr = merge_sort_stack(arr)

print("Sorted:", sorted_arr)