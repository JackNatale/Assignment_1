def solution(A):
    eastbound = 0  # eastbound cars (0s) seen so far
    pairs = 0      # total passing pairs found so far

    for car in A:
        if car == 0:
            # Another eastbound car that future westbound cars can pass
            eastbound += 1
        else:
            # This westbound car passes all eastbound cars seen before it
            pairs += eastbound

        # The problem caps the answer at 1,000,000,000; stop early if exceeded
        if pairs > 1000000000:
            return -1

    return pairs