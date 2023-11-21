# Count distinct substrings of a string using Rabin Karp algorithm
def count_distinct_substrings(s):
    distinct_substrings = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            distinct_substrings.add(s[i:j + 1])
    return len(distinct_substrings)

# Example
input_str = "abacabadabacaba"
result = count_distinct_substrings(input_str)
print("Count of distinct substrings:", result)
