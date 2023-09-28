def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def is_symmetrical(s):
    s = s.replace(" ", "")
    return s == s[::-1]

input_string = input("Enter a string: ")


if is_palindrome(input_string):
    print("It's a palindrome.")
elif is_symmetrical(input_string):
    print("It's symmetrical but not a palindrome.")
else:
    print("It's neither a palindrome nor symmetrical.")
