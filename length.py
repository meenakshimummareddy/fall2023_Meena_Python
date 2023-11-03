def unique_elements(lst):
    unique = list(set(lst))
    return unique

# Example
my_list = [1, 2, 3, 2, 4, 5, 1, 3, 6]
result = unique_elements(my_list)
print("Unique elements in the list:", result)
