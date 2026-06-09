def postorder_traverse(tree):

    stack = []

    ptr = 0      # Root index

    last_visited = None

    print("Postorder Traversal:", end=" ")

    while stack or ptr is not None:

        # Move to leftmost node
        while ptr is not None:

            stack.append(ptr)

            left = 2 * ptr + 1

            if left < len(tree) and tree[left] is not None:
                ptr = left
            else:
                ptr = None

        # Peek top node
        peek = stack[-1]

        right = 2 * peek + 2

        # If right child exists and has not been visited
        if (right < len(tree) and tree[right] is not None and last_visited != right):

            ptr = right

        else:

            print(tree[peek], end=" ")

            last_visited = stack.pop()

    print()


tree = ['A','B','C','D','E','F','G',None,'H',None,None,'I','J']


postorder_traverse(tree)