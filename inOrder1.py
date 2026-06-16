def inorder_traverse(tree):

    # Step 1
    stack = [None] * 100

    stack[0] = None
    top = 1

    ptr = 0      # Root

    # Step 2
    while ptr is not None:

        # Step 2(a), 2(b)
        while ptr is not None:

            stack[top] = ptr
            top += 1

            ptr_left = 2 * ptr + 1

            if tree[ptr_left] is not None  and ptr_left < len(tree) :
                ptr = ptr_left
            else:
                ptr = None

        # Step 3
        top -= 1
        ptr = stack[top]

        # Step 4
        while ptr is not None:

            # Step 5
            print(tree[ptr], end=" ")

            # Step 6
            ptr_right = 2 * ptr + 2

            if ptr_right < len(tree) and tree[ptr_right] is not None:

                ptr = ptr_right

                # go back to Step 2
                while ptr is not None:

                    stack[top] = ptr
                    top += 1

                    left = 2 * ptr + 1

                    if left < len(tree) and tree[left] is not None:
                        ptr = left
                    else:
                        ptr = None

                top -= 1
                ptr = stack[top]

            else:

                # Step 7
                top -= 1
                ptr = stack[top]

tree = ['A', 'B', 'C', 'D', 'E', 'F', 'G', None, 'H', None, None, 'I', 'J']

inorder_traverse(tree)