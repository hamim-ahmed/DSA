class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class HashTable:

    def __init__(self, size):

        self.size = size

        # Hash table array
        self.table = [None] * size

    # Simple Hash Function
    def hash_function(self, key):

        return key % self.size

    # Insert with Chaining
    def insert(self, key):

        index = self.hash_function(key)

        print(f"\nKey {key} -> Index {index}")

        new_node = Node(key)

        # No collision
        if self.table[index] is None:

            self.table[index] = new_node

            print("Inserted without collision")

        # Collision occurs
        else:

            print("Collision occurred")
            print("Applying chaining...")

            temp = self.table[index]

            # Move to end of linked list
            while temp.next:

                temp = temp.next

            temp.next = new_node

            print(f"{key} added in linked list")

    # Display Hash Table
    def display(self):

        print("\nHash Table:\n")

        for i in range(self.size):

            print(f"Index {i} --> ", end="")

            temp = self.table[i]

            if temp is None:

                print("None")

            else:

                while temp:

                    print(temp.data, end=" -> ")

                    temp = temp.next

                print("None")


# ---------------- MAIN ----------------

size = int(input("Enter hash table size: "))

ht = HashTable(size)

n = int(input("How many keys? "))

for _ in range(n):

    key = int(input("Enter key: "))

    ht.insert(key)

ht.display()