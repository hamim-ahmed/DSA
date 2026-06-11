def preorder_traverse(tree):

    stack = []

    ptr = 0      # Root index

    print("Preorder Traversal:", end=" ")


    while ptr is not None:


        # Process current node
        print(tree[ptr], end=" ")

        # to Push right child
        ptr_right = 2 * ptr + 2

        if tree[ptr_right] is not None and ptr_right < len(tree) :   #if right child within the array length and not none
            stack.append(ptr_right)

        # Move to left child
        ptr_left = 2 * ptr + 1

        if tree[ptr_left] is not None and ptr_left < len(tree) :

            ptr = ptr_left

        else:

            if stack:
                ptr = stack.pop()

            else:
                ptr = None



tree = ['A','B','C','D','E','F','G',None,'H',None,None,'I','J']


preorder_traverse(tree)