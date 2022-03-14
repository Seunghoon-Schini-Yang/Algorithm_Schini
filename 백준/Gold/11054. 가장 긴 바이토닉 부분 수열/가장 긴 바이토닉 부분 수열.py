import sys
input = sys.stdin.readline

def solution(n: int, arr: list) -> int:
    inc_dp, dec_dp = [1] * n, [1] * n
    inc_seq, dec_seq = [arr[0]], [arr[-1]]

    for i, j in enumerate(range(-2, -n-1, -1), start=1):
        if arr[i] > inc_seq[-1]:
            inc_seq.append(arr[i])
        else:
            inc_seq[binary_search(0, len(inc_seq) - 1, arr[i], inc_seq)] = arr[i]

        if arr[j] > dec_seq[-1]:
            dec_seq.append(arr[j])
        else:
            dec_seq[binary_search(0, len(dec_seq) - 1, arr[j], dec_seq)] = arr[j]

        inc_dp[i], dec_dp[i] = len(inc_seq), len(dec_seq)
    
    maxi = max(inc_dp[i] + dec_dp[n - 1 - i] - 1 for i in range(n))

    return maxi


def binary_search(l: int, r: int, arr_i: int, seq: list) -> int:
    while l <= r:
        m = (l + r) // 2

        if arr_i <= seq[m]:
            r = m - 1
        else:
            l = m + 1
    return l
    

print(solution(int(input()), list(map(int, input().split()))))
