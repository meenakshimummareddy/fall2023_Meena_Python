# AND Operation between Tuples Function
def tuple_and(tup1, tup2):
    return tuple(a & b for a, b in zip(tup1, tup2))

# Example
tuple1 = (1, 0, 1, 0)
tuple2 = (0, 1, 0, 1)
result = tuple_and(tuple1, tuple2)
print("AND operation between Tuples:", result)
