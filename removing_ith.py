def remove_character(input_string, i):
    # Check if the index is valid
    if i < 0 or i >= len(input_string):
        return "Invalid index"

    # Remove the i-th character by slicing
    result_string = input_string[:i] + input_string[i+1:]

    return result_string

input_string = input("Enter a string: ")
i = int(input("Enter the index of the character to remove: "))

result = remove_character(input_string, i)

if result != "Invalid index":
    print("String after removing character:", result)
else:
    print("Invalid index. Please enter a valid index within the string's length.")
