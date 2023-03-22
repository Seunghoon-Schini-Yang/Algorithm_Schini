import sys
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    memo = {0: 0}
    for _ in range(N):
        W, V = map(int, input().split())
        tmp = {}
        for v, w in memo.items():
            if w+W > memo.get(v+V, K):
                continue
            tmp[v+V] = w+W
        memo.update(tmp)
    print(max(memo.keys()))


if __name__ == '__main__':
    main()