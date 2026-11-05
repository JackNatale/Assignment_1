def solution(A):
    # Start at 0, since XOR with 0 leaves a number unchanged
    result = 0

    # XOR each number into the running result
    for number in A:
        result ^= number

    # All pairs have cancelled out; what's left is the unpaired value
    return result
