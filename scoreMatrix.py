# Scoring Matrix using Dictionary
scoring_matrix = {
    ('A', 'A'): 2, ('A', 'C'): -1, ('A', 'G'): -1, ('A', 'T'): -1,
    ('C', 'A'): -1, ('C', 'C'): 2, ('C', 'G'): -1, ('C', 'T'): -1,
    ('G', 'A'): -1, ('G', 'C'): -1, ('G', 'G'): 2, ('G', 'T'): -1,
    ('T', 'A'): -1, ('T', 'C'): -1, ('T', 'G'): -1, ('T', 'T'): 2
}

# Example
print("Scoring matrix value for ('A', 'G'):", scoring_matrix[('A', 'G')])
