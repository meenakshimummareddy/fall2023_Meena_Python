# Skew Nested Tuple Summation Function
def nested_tuple_sum(tup):
    result = 0
    for i, item in enumerate(tup):
        if isinstance(item, tuple):
            result += nested_tuple_sum(item) * (i + 1)
        else:
            result += item * (i + 1)
    return result

# Example
nested_tuple = ((1, 2), 3, (4, (5, 6)))
result = nested_tuple_sum(nested_tuple)
print("Skew Nested Tuple Summation:", result)
