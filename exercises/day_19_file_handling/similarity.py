from difflib import SequenceMatcher
from math import sqrt
# ---- Jaccard Similarity ----
def jaccard_similarity(file1, file2):
    set1 = set(file1)
    set2 = set(file2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if not union:
        return 0.0
    return len(intersection) / len(union)

# ---- Cosine Similarity ----
def cosine_similarity(file1, file2):
    freq1 = {}
    freq2 = {}

    for word in file1:
        freq1[word] = freq1.get(word, 0) + 1
    for word in file2:
        freq2[word] = freq2.get(word, 0) + 1

    intersection = set(freq1.keys()) & set(freq2.keys())
    numerator = sum(freq1[word] * freq2[word] for word in intersection)

    sum1 = sum(v**2 for v in freq1.values())
    sum2 = sum(v**2 for v in freq2.values())
    denominator = sqrt(sum1) * sqrt(sum2)

    if denominator == 0:
        return 0.0
    return numerator / denominator

# ---- SequenceMatcher Similarity ----
def sequence_similarity(file1, file2):
    return SequenceMatcher(None, file1, file2).ratio()