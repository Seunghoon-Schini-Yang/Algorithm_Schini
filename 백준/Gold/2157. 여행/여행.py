import sys
input = sys.stdin.readline


def main():
    N, M, K = map(int, input().split())
    paths = [{} for _ in range(N+1)]
    for _ in range(K):
        a, b, c = map(int, input().split())
        if a >= b or c <= paths[a].get(b, 0):
            continue
        paths[a][b] = c

    answer = 0
    memo = {1: 0}
    for _ in range(M-1):
        cur = {}
        for depart, acc in memo.items():
            for arrive, score in paths[depart].items():
                cur[arrive] = max(acc + score, cur.get(arrive, 0))
        memo = cur
        answer = max(answer, memo.get(N, 0))
    print(answer)


if __name__ == '__main__':
    main()
