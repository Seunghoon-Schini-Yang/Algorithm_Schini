import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    bs = [i for i in range(N+1)]
    for _ in range(M):
        i, j, k = map(int, input().split())
        bs[i:j+1] = bs[k:j+1] + bs[i:k]
    print(*bs[1:])


if __name__ == '__main__':
    main()