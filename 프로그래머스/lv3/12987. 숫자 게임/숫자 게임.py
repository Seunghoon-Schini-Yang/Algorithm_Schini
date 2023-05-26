def solution(A, B):
    A.sort()
    B.sort()
    i = score = 0
    for b in B:
        if A[i] < b:
            i += 1
            score += 1
    return score