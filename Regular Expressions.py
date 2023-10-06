import re

# Sample text with email addresses and phone numbers
text = """
John's email is john@example.com, and his phone number is +1 (555) 555-5555.
Mary can be reached at mary@gmail.com, or her phone at 123-456-7890.
"""

# Define regex patterns
email_pattern = r'\S+@\S+'
phone_pattern = r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

# Find and print emails
emails = re.findall(email_pattern, text)
print("Email Addresses:")
for email in emails:
    print(email)

# Find and print phone numbers
phone_numbers = re.findall(phone_pattern, text)
print("\nPhone Numbers:")
for phone in phone_numbers:
    print(phone)
