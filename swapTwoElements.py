def swap_elements(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

# Example
my_list = [10, 20, 30, 40, 50]
result = swap_elements(my_list, 1, 3)
print("List after swapping elements:", result)
