# Convert Binary tuple to Integer Function
def binary_tuple_to_int(tup):
    binary_str = ''.join(str(i) for i in tup)
    return int(binary_str, 2)

# Example
binary_tuple = (1, 0, 0, 1, 1)
result = binary_tuple_to_int(binary_tuple)
print("Binary tuple converted to Integer:", result)
