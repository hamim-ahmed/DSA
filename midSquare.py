def mid_square_hash(key, table_size):

    square = key * key

    square_str = str(square)        # Convert to string
    print("Square value:", square_str)

    mid = len(square_str) // 2          # Step 2: Find middle digits


    if len(square_str) >= 2:                                #if the square value is less than 2 digit.
        middle_digits = square_str[mid-1:mid+1]
        # print(mid-1, mid+1)
        print("middle digits:", middle_digits)

    else:
        middle_digits = square_str
        print("middle digits:", middle_digits)

    hash_value = int(middle_digits)

    # Compress into table size
    return hash_value % table_size


# Main Program
table_size = int(input("Enter hash table size: "))

key = int(input("Enter key: "))

result = mid_square_hash(key, table_size)

print("Hash Value:", result)