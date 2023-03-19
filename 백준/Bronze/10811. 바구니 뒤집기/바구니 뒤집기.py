import sys
input = sys.stdin.readline


def main(N, M):
    baskets = [i for i in range(1, N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        baskets[s-1:e] = baskets[s-1:e][::-1]
    print(*baskets)


if __name__ == '__main__':
    main(*map(int, input().split()))
