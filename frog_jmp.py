def solution(X, Y, D):
    # Total distance the frog needs to cover
    distance = Y - X

    # Number of full jumps that fit into the distance
    jumps = distance // D

    # If there is a remainder, the frog falls short after the full jumps,
    # so one more jump is required to reach or pass Y
    if distance % D != 0:
        jumps += 1

    return jumps
