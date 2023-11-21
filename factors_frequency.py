# Factors Frequency Dictionary
def factors_frequency_dict(n):
    factors = {}
    for i in range(1, n + 1):
        if n % i == 0:
            factors[i] = factors.get(i, 0) + 1
    return factors

# Example
num = 30
result = factors_frequency_dict(num)
print("Factors frequency dictionary for", num, ":", result)
