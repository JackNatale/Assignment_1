def solution(A):
    eastbound = 0
    pairs = 0

    for car in A:
        if car == 0:
            eastbound += 1
        else:
            pairs += eastbound

        if pairs > 1000000000:
            return -1

    return pairs