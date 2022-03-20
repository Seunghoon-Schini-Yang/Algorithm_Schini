import sys
input = sys.stdin.readline


def solution():
    m, k = map(int, input().split())
    m_1 = [list(map(int, input().split())) for _ in range(m)]

    k, n = map(int, input().split())
    m_2 = [list(map(int, input().split())) for _ in range(k)]

    for row in range(m):
        for col in range(n):
            print(sum(m_1[row][i] * m_2[i][col] for i in range(k)), end=' ')
        print()


solution()
