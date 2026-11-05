
def solution(A):
    total = sum(A)        # Sum of the whole array
    left = 0              # Running sum of the left part
    best = float('inf')   # Smallest difference found so far

    # Stop at len(A) - 1 so the right part has at least one element
    for i in range(len(A) - 1):
        # Move element i from the right part to the left part
        left += A[i]
        right = total - left

        # Absolute difference between the two parts for this split
        difference = abs(left - right)

        # Keep the smallest difference seen
        best = min(best, difference)

    return best
