def solution(e, starts):
    memo = [0] * (e+1)
    e_sqrt = int(pow(e, 0.5))
    for n in range(1, e_sqrt+1):
        memo[n*n] += 1
        for i in range(n*(n+1), e+1, n):
            memo[i] += 2

    max_val = max_num = 0
    for i in range(e, 0, -1):
        if memo[i] >= max_val:
            max_val, max_num = memo[i], i
        memo[i] = max_num

    for i, start in enumerate(starts):
        starts[i] = memo[start]

    return starts
