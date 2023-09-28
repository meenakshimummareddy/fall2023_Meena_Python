def reverse_words(input_string):
    words = input_string.split()  # Split the input string into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_string = " ".join(reversed_words)  # Join the reversed words back into a string
    return reversed_string

input_string = input("Enter a string: ")
result = reverse_words(input_string)
print("Reversed string with reversed words:", result)
