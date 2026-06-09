def preorder_traverse(tree):

    stack = []

    ptr = 0      # Root index

    print("Preorder Traversal:", end=" ")


    while ptr is not None:

        print(" [", end=" ")
        for index in stack:
            if stack is not None:
                print(tree[index], end=" ")
        print("]", end=" ")

        # Process current node
        print(tree[ptr])

        # to Push right child
        right = 2 * ptr + 2

        if right < len(tree) and tree[right] is not None:   #if right child within the array length and not none
            stack.append(right)

        # Move to left child
        left = 2 * ptr + 1

        if left < len(tree) and tree[left] is not None:

            ptr = left

        else:

            if stack:
                ptr = stack.pop()

            else:
                ptr = None



tree = ['A','B','C','D','E','F','G',None,'H',None,None,'I','J']


preorder_traverse(tree)