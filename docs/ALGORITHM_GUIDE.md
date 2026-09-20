# Algorithm guide

Start with the lookup-table example below. This is an implementation-specific
card, not an assertion that every exercise in this collection has been audited.
Arithmetic and dictionary keys are treated as fixed-width values.

## Power-of-two pairs

Implementation: [`solution`](../Code%20Signal/lookup_table.py).

```text
# CodeSignal / Frequency Lookup for Power-of-Two Pairs
# Goal: count index pairs (i, j), i <= j, whose sum is an enumerated power of two.
# Input: N integers
# Output: number of qualifying pairs
# Time: expected O(N*P); P=21 in this implementation, so expected O(N)
# Memory: O(N*P) dictionary keys in general; O(N) with fixed P=21
# P enumerates powers 2^0 through 2^20, inclusive

counts = default-zero dictionary
answer = 0
FOR each x in input order:
    counts[x] += 1
    FOR exponent from 0 through 20:
        complement = (1 << exponent) - x
        answer += counts[complement]
RETURN answer
```

Why insertion comes first: it permits the current element to pair with itself.
Earlier indices are already counted, while later indices are not, so qualifying
unordered index pairs are counted once.

Example: `[1, 1]` returns 3: `(0,0)`, `(0,1)`, `(1,1)`. Empty input returns 0.
The code does not dynamically enlarge the power range for larger values.

## Memory and assumptions

`defaultdict(int)` inserts a zero entry when a missing complement is read.
The map can therefore store absent complement values as well as observed input
values. O(number of distinct input values) alone is not a sufficient general
bound; there are at most O(NP) inserted keys.

Expected time assumes ordinary hash-table behavior. If arbitrary-size integers
are admitted, hashing, shifting, addition and subtraction have bit-length costs.
P is fixed in this code, so `O(N log(max_value))` describes a possible dynamic
power enumeration, not the current implementation.

This guide changes documentation only. A version counting only `i < j` would
need to insert `x` after looking up complements, which is not done here.
