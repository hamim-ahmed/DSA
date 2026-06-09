from itertools import combinations


def apriori(transactions, min_support):
    item_counts = {}

    # 🔹 Step 1: Count 1-itemsets
    for transaction in transactions:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    num_transactions = len(transactions)
    frequent_items = {}

    # 🔹 Step 2: Filter by min_support
    for item, count in item_counts.items():
        support = count / num_transactions
        if support >= min_support:
            frequent_items[frozenset([item])] = support

    all_frequent_itemsets = dict(frequent_items)
    k = 2

    # 🔹 Step 3: Iteratively generate k-itemsets
    while frequent_items:
        candidates = generate_candidates(frequent_items.keys(), k)

        candidate_counts = {}

        for transaction in transactions:
            transaction_set = set(transaction)
            for candidate in candidates:
                if candidate.issubset(transaction_set):
                    candidate_counts[candidate] = candidate_counts.get(candidate, 0) + 1

        frequent_items = {}

        for candidate, count in candidate_counts.items():
            support = count / num_transactions
            if support >= min_support:
                frequent_items[candidate] = support

        all_frequent_itemsets.update(frequent_items)
        k += 1

    return all_frequent_itemsets


# 🔹 Improved Candidate Generation (No duplicates + pruning)
def generate_candidates(prev_itemsets, k):
    candidates = set()
    prev_itemsets = list(prev_itemsets)

    for i in range(len(prev_itemsets)):
        for j in range(i + 1, len(prev_itemsets)):
            l1 = list(prev_itemsets[i])
            l2 = list(prev_itemsets[j])

            l1.sort()
            l2.sort()

            # 🔹 Join step: only if first k-2 items match
            if l1[:k - 2] == l2[:k - 2]:
                union_set = prev_itemsets[i] | prev_itemsets[j]

                if len(union_set) == k:
                    # 🔹 Prune step: all (k-1)-subsets must be frequent
                    subsets = combinations(union_set, k - 1)
                    if all(frozenset(subset) in prev_itemsets for subset in subsets):
                        candidates.add(union_set)

    return list(candidates)


# 🔹 Input (your dataset)
def get_transactions():
    # transactions = []
    # n = int(input("Enter number of transactions: "))
    #
    # for i in range(n):
    #     user_input = input(f"Enter items for transaction {i + 1} (comma separated): ")
    #     items = [item.strip() for item in user_input.split(",")]
    #     transactions.append(items)

    transactions = [
        ["br", "btr", "jam", "milk"],
        ["br", "btr", "milk"],
        ["br", "juice", "curd"],
        ["br", "milk", "juice"],
        ["br", "btr", "milk", "juice"]
    ]
    return transactions


# 🔹 Main
transactions = get_transactions()
min_support = float(input("Enter minimum support (e.g., 0.5): "))

result = apriori(transactions, min_support)

print("\nFrequent Itemsets:")
for itemset, support in result.items():
    print(set(itemset), "->", round(support, 2))