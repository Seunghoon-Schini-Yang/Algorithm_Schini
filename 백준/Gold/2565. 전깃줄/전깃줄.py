import sys
input = sys.stdin.readline


def std_input(n: int) -> int:
    cord_list = [tuple(map(int, input().split())) for _ in range(n)]
    return solution(n, cord_list)


def solution(n: int, arr: list) -> int:
    arr.sort()
    dp = [arr[0][1]]

    for i in range(1, n):
        if arr[i][1] > dp[-1]:
            dp.append(arr[i][1])
        else:
            dp[binary_search(0, len(dp) - 1, arr[i][1], dp)] = arr[i][1]
    
    return n - len(dp)


def binary_search(l: int, r: int, arr_i: int, seq: list) -> int:
    while l <= r:
        m = (l + r) // 2

        if arr_i < seq[m]:
            r = m - 1
        else:
            l = m + 1
    return l


print(std_input(int(input())))
