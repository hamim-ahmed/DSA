import json
import urllib.request


# ==================================================
# NODE CREATION
# ==================================================

def create_node(order, is_leaf):
    return {
        "order": order,
        "is_leaf": is_leaf,
        "keys": [],
        "children": [],
        "records": [],      # only used in leaf nodes
        "next": None
    }


# ==================================================
# TREE CREATION
# ==================================================

def create_tree(order):
    return {
        "order": order,
        "root": create_node(order, True)
    }


# ==================================================
# INSERT INTO LEAF
# ==================================================

def insert_into_leaf(leaf, word, meaning):

    # update existing word if already present
    for i, (w, _) in enumerate(leaf["records"]):
        if w == word:
            leaf["records"][i] = (word, meaning)
            return

    leaf["records"].append((word, meaning))

    leaf["records"].sort(key=lambda x: x[0])

    leaf["keys"] = [record[0] for record in leaf["records"]]


# ==================================================
# SPLIT LEAF
# ==================================================

def split_leaf(leaf):

    order = leaf["order"]

    mid = order // 2

    left_leaf = leaf

    right_leaf = create_node(order, True)

    right_leaf["records"] = left_leaf["records"][mid:]
    left_leaf["records"] = left_leaf["records"][:mid]

    left_leaf["keys"] = [r[0] for r in left_leaf["records"]]
    right_leaf["keys"] = [r[0] for r in right_leaf["records"]]

    right_leaf["next"] = left_leaf["next"]
    left_leaf["next"] = right_leaf

    promoted_key = right_leaf["keys"][0]

    return promoted_key, right_leaf


# ==================================================
# SPLIT INTERNAL NODE
# ==================================================

def split_internal(node):

    order = node["order"]

    mid = order // 2

    left_node = node

    right_node = create_node(order, False)

    promote_key = left_node["keys"][mid]

    right_node["keys"] = left_node["keys"][mid + 1:]
    left_node["keys"] = left_node["keys"][:mid]

    right_node["children"] = left_node["children"][mid + 1:]
    left_node["children"] = left_node["children"][:mid + 1]

    return promote_key, right_node


# ==================================================
# RECURSIVE INSERT
# ==================================================

def insert_recursive(node, word, meaning):

    if node["is_leaf"]:

        insert_into_leaf(node, word, meaning)

        if len(node["keys"]) < node["order"]:
            return None, None

        return split_leaf(node)

    i = 0

    while i < len(node["keys"]) and word >= node["keys"][i]:
        i += 1

    promoted, new_child = insert_recursive(
        node["children"][i],
        word,
        meaning
    )

    if new_child is None:
        return None, None

    node["keys"].insert(i, promoted)
    node["children"].insert(i + 1, new_child)

    if len(node["keys"]) < node["order"]:
        return None, None

    return split_internal(node)


# ==================================================
# INSERT
# ==================================================

def insert(tree, word, meaning):

    root = tree["root"]

    promoted, new_child = insert_recursive(
        root,
        word,
        meaning
    )

    if new_child is not None:

        new_root = create_node(
            tree["order"],
            False
        )

        new_root["keys"] = [promoted]

        new_root["children"] = [
            root,
            new_child
        ]

        tree["root"] = new_root


# ==================================================
# SEARCH
# ==================================================

def search(node, word):

    if node["is_leaf"]:

        for stored_word, meaning in node["records"]:

            if stored_word == word:
                return meaning

        return None

    i = 0

    while i < len(node["keys"]) and word >= node["keys"][i]:
        i += 1

    return search(node["children"][i], word)


# ==================================================
# DISPLAY TREE
# ==================================================

def display(node, level=0):

    print("Level", level, ":", node["keys"][:10],
          "..." if len(node["keys"]) > 10 else "")

    if not node["is_leaf"]:

        for child in node["children"]:
            display(child, level + 1)


# ==================================================
# COUNT HEIGHT
# ==================================================

def tree_height(node):

    if node["is_leaf"]:
        return 1

    return 1 + tree_height(node["children"][0])


# ==================================================
# LOAD DICTIONARY FROM URL
# ==================================================

def load_dictionary(url):

    with urllib.request.urlopen(url) as response:

        return json.loads(
            response.read().decode("utf-8")
        )


# ==================================================
# MAIN
# ==================================================

url = input("Enter dictionary JSON URL:\n")

order = int(
    input("Enter B+ Tree Order (recommended 50-100): ")
)

print("\nLoading dictionary...")

dictionary_data = load_dictionary(url)

print("Total words loaded:", len(dictionary_data))

tree = create_tree(order)

print("\nBuilding B+ Tree...")

count = 0

for word, meaning in dictionary_data.items():

    insert(
        tree,
        word.lower(),
        meaning
    )

    count += 1

    if count % 5000 == 0:
        print(count, "words indexed...")

print("\nB+ Tree Build Complete")
print("Height:", tree_height(tree["root"]))

print("\nRoot Keys:")
print(tree["root"]["keys"][:20])

# Uncomment if you want full tree structure
# display(tree["root"])

print("\nDictionary Ready")


# ==================================================
# SEARCH LOOP
# ==================================================
import time
while True:

    word = input(
        "\nEnter word (or 'exit'): "
    ).strip().lower()

    if word == "exit":
        break

    #result = search(tree["root"],word)

    start = time.perf_counter()

    result = search(tree["root"], word)

    end = time.perf_counter()

    # print(f"\nSearch Time: {(end - start):.9f} seconds")

    if result:
        print("\nMeaning:\n")
        print(result)

    else:
        print("\nWord not found.")

#https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json