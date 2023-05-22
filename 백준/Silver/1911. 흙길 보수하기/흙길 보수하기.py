import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, L = map(int, input().split())
    cnt = c = 0
    for s, e in sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0]):
        s = c if s < c else s
        d = e - s
        if not d:
            continue
        t = ((d-1)//L)+1
        cnt += t
        c = t*L + s
    print(cnt)