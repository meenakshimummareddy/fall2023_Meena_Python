def swap_elements_str_list(lst, el1, el2):
    index1 = lst.index(el1)
    index2 = lst.index(el2)
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

# Example
my_list = ['apple', 'banana', 'cherry', 'date']
result = swap_elements_str_list(my_list, 'banana', 'cherry')
print("List after swapping elements:", result)
