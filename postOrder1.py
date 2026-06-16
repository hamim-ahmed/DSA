def postorder_traverse(tree):

    if not tree or tree[0] is None:
        return

    stack1 = [0]      # root index
    stack2 = []

    print("Postorder Traversal:", end=" ")

    while stack1:

        # Step 2.1
        ptr = stack1.pop()
        stack2.append(ptr)

        # Step 2.2
        ptr_left = 2 * ptr + 1
        ptr_right = 2 * ptr + 2

        # Push left first, then right
        if ptr_left < len(tree) and tree[ptr_left] is not None:
            stack1.append(ptr_left)

        if ptr_right < len(tree) and tree[ptr_right] is not None:
            stack1.append(ptr_right)

    # Step 3
    while stack2:

        ptr = stack2.pop()
        print(tree[ptr], end=" ")

    print()


tree = ['A','B','C','D','E','F','G',None,'H',None,None,'I','J']

postorder_traverse(tree) 