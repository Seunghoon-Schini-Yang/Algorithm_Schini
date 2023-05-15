def solution(n):
    memo = [1, 1, 3, 10, 23, 62]
    if n <= 5:  return memo[n]
    four = [2, 2, 0]
    five = [2, 0, 0]
    six = [0, 0, 0]
    for i in range(6, n+1):
        cur = memo[-1] + 2*memo[-2] + 5*memo[-3]
        idx = (i-2)%3
        five[idx] += memo[1] << 1
        cur += five[idx]
        idx = (i-1)%3
        four[idx] += memo[2] << 1
        cur += four[idx]
        idx = i%3
        six[idx] += memo[0] << 2
        cur += six[idx]
        memo = memo[1:] + [cur]
    return memo[-1] % 1_000_000_007
