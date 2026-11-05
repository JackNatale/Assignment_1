def solution(A):
    N = len(A)
    seen = set()    # values encountered so far

    for number in A:
        # Out of range: a permutation of length N only holds values 1..N
        if number < 1 or number > N:
            return 0

        # Duplicate: each value must appear exactly once
        if number in seen:
            return 0

        # Record this value as seen
        seen.add(number)

    # All values were in range and unique, so A is a permutation
    return 1
