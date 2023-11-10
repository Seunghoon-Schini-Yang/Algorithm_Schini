import sys
input = sys.stdin.readline
from collections import deque

        
def main():
    N, M, L, K = map(int, input().split())
    stars = [tuple(map(int, input().split())) for _ in range(K)]
    stars.sort(key=lambda x: x[0])
    dq = deque()
    maxy, i = 1, 0
    while i < K:
        if not dq:
            dq.append(stars[i])
            i += 1
        while i < K and stars[i][0] <= dq[0][0] + L:
            dq.append(stars[i])
            i += 1
        
        cur = [y for _, y in dq]
        cur.sort()
        l = r = 0
        while r < len(cur):
            while r < len(cur) and cur[r] - cur[l] <= L:
                r += 1
            maxy = max(maxy, r-l)
            if r == len(cur):
                break
            while cur[r] - cur[l] > L:
                l += 1
        
        if i == K:
            break
        while dq and stars[i][0] - dq[0][0] > L:
            dq.popleft()
    print(K - maxy)


if __name__ == '__main__':
    main()
