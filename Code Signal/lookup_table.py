# CodeSignal / Lookup Table / Power-of-Two Pairs
# Count pairs (i, j) with i <= j where numbers[i] + numbers[j] is a power of 2.
# Time: expected O(n * P); P=21 fixed here, so expected O(n).
# Memory: O(n * P) possible dictionary keys; O(n) for fixed P.
# Pseudocode: insert current value, then sum prior/current complement counts.
# Reading a missing defaultdict complement also inserts a zero-valued key.
# Power range and edge cases: docs/ALGORITHM_GUIDE.md.

from collections import defaultdict


# Insert first to include self-pairs; insert last instead for i < j.
def solution(numbers):
    counts = defaultdict(int)
    answer = 0
    for element in numbers:
        counts[element] += 1
        for two_power in range(21):           # Exact sum range: 2^0 through 2^20.
            second_element = (1 << two_power) - element
            answer += counts[second_element]  # Includes the current element if it pairs.
    return answer
