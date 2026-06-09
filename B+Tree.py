# ----------- NODE -----------
def create_node(order, is_leaf):
    return {
        "order": order,
        "is_leaf": is_leaf,
        "keys": [],
        "children": [],
        "next": None
    }


# ----------- TREE -----------
def create_tree(order):
    return {
        "order": order,
        "root": create_node(order, True)
    }




# ----------- INSERT INTO LEAF -----------
def insert_into_leaf(leaf, key):
    leaf["keys"].append(key)
    leaf["keys"].sort()


# ----------- SPLIT LEAF -----------
def split_leaf(left_leaf):
    order = left_leaf["order"]
    mid = order // 2

    # create right leaf
    right_leaf = create_node(order, True)    #creating a new node for the right leaf.

    # split keys
    right_leaf["keys"] = left_leaf["keys"][mid:]
    left_leaf["keys"] = left_leaf["keys"][:mid]

    # fix linked list
    right_leaf["next"] = left_leaf["next"]
    left_leaf["next"] = right_leaf

    # promote first key of right leaf
    return right_leaf["keys"][0], right_leaf


# ----------- SPLIT INTERNAL -----------
def split_internal(left_node):
    order = left_node["order"]
    mid = order // 2

    # create right internal node
    right_node = create_node(order, False)

    # key to promote
    promote_key = left_node["keys"][mid]

    # split keys
    right_node["keys"] = left_node["keys"][mid+1:]
    left_node["keys"] = left_node["keys"][:mid]

    # split children
    right_node["children"] = left_node["children"][mid+1:]
    left_node["children"] = left_node["children"][:mid+1]

    return promote_key, right_node


# ----------- INSERT RECURSIVE -----------
def insert_recursive(node, key):                #insert logic whether split or direct insert.
    if node["is_leaf"]:
        insert_into_leaf(node, key)             # if current node is a leaf. direct insert the key into leaf and sort.

        if len(node["keys"]) < node["order"]:   #if no of keys in leaf is less than the order....no split still space left to insert
            return None, None

        return split_leaf(node)

    i = 0
    while i < len(node["keys"]) and key >= node["keys"][i]:
        i += 1

    promoted, right_child = insert_recursive(node["children"][i], key)

    if right_child is None:
        return None, None

    node["keys"].insert(i, promoted)
    node["children"].insert(i + 1, right_child)

    if len(node["keys"]) < node["order"]:
        return None, None

    return split_internal(node)


# ----------- INSERT -----------
def insert(tree, key):
    root = tree["root"]

    promoted, right_child = insert_recursive(root, key)

    if right_child is not None:
        new_root = create_node(tree["order"], False)
        new_root["keys"] = [promoted]
        new_root["children"] = [root, right_child]
        tree["root"] = new_root


# ----------- DISPLAY -----------
def display(node, level=0):
    print("Level", level, ":", node["keys"])

    if not node["is_leaf"]:
        for child in node["children"]:
            display(child, level + 1)


# ----------- MAIN -----------
order = int(input("Enter order of B+ Tree: "))
tree = create_tree(order)

data = [40,10,50,30,90,80,70,20,60,100,105]
print("Input array:", data)

for v in data:
    insert(tree, v)

print("\nB+ Tree structure:")
display(tree["root"])