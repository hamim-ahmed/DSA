def inorder_traverse(tree):

    stack = []

    ptr = 0      # Root index

    print("Inorder Traversal:", end=" ")

    while True:

        # Move to leftmost node
        while ptr is not None:

            stack.append(ptr)

            left = 2 * ptr + 1

            if left < len(tree) and tree[left] is not None:
                ptr = left
            else:
                ptr = None

        # If stack empty, traversal finished
        if not stack:
            break

        # Step 3
        ptr = stack.pop()

        # Step 5
        print(tree[ptr], end=" ")

        # Step 6
        right = 2 * ptr + 2

        if right < len(tree) and tree[right] is not None:

            ptr = right

        else:

            ptr = None

    print()


tree = ['A','B','C','D','E','F','G',None,'H',None,None,'I','J']


inorder_traverse(tree)