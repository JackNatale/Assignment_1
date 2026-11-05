def solution(X, Y, D):
    distance = Y - X

    jumps = distance // D

    if distance % D != 0:
        jumps += 1

    return jumps
