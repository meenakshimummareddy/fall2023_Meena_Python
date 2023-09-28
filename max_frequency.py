def max_frequency_char(input_string):
    # Create an empty dictionary to store character frequencies
    char_count = {}

    # Iterate through the string and count character frequencies
    for char in input_string:
        if char.isalpha():  # Only consider alphabet characters
            char_count[char] = char_count.get(char, 0) + 1

    # Find the character with the maximum frequency
    max_char = max(char_count, key=char_count.get)
    max_freq = char_count[max_char]

    return max_char, max_freq

input_string = input("Enter a string: ")
max_char, max_freq = max_frequency_char(input_string)

print(f"The character '{max_char}' has the maximum frequency of {max_freq} times.")
