def folding_hash(key, table_size):

    key_str = str(key)

    parts = []

    # Split into groups of 2 digits
    for i in range(0, len(key_str), 2):

        part = key_str[i:i+2]

        parts.append(int(part))
    print("parts:", parts)
    # Add all parts
    total = sum(parts)

    return total % table_size


# Main Program
table_size = int(input("Enter hash table size: "))

key = int(input("Enter key: "))

result = folding_hash(key, table_size)

print("Hash Value:", result)