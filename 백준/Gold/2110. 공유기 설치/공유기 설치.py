import sys
input = sys.stdin.readline

def solution(n: int, c: int) -> int:
    xs = [int(input()) for _ in range(n)]
    xs.sort()

    start, end = 1, xs[-1]//(c-1) + 1
    minys = list()

    while start <= end:
        cnt = 1
        cx = xs[0]
        mid = (start + end) // 2

        for i in range(1, n):
            if xs[i] >= cx + mid:
                cnt += 1
                cx = xs[i]

        if cnt >= c:
            start = mid + 1
        else:
            end = mid - 1

    return end


print(solution(*map(int, input().split())))
