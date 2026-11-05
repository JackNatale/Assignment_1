def solution(A):
    total = sum(A)
    left = 0
    best = float('inf')

    for i in range(len(A) -1):
        left += A[i]
        right = total - left

        difference = abs(left - right)
        best = min(best, difference)

    return best
