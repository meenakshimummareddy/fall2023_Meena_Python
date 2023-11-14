# Elementwise AND in Tuples Function
def elementwise_and(tup1, tup2):
    return tuple(x & y for x, y in zip(tup1, tup2))

# Example
tuple1 = (1, 0, 1, 0)
tuple2 = (0, 1, 0, 1)
result = elementwise_and(tuple1, tuple2)
print("Elementwise AND in Tuples:", result)
