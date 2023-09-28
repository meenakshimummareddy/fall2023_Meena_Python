from itertools import permutations

def generate_permutations(input_string):
    # Generate all permutations of the input string
    permuted_strings = permutations(input_string)

    # Convert the permutations to a list of strings
    permuted_strings = [''.join(perm) for perm in permuted_strings]

    return permuted_strings

input_string = input("Enter a string: ")

permutations_list = generate_permutations(input_string)

print("Permutations of the string:")
for permuted_string in permutations_list:
    print(permuted_string)
