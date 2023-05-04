import sys
input = sys.stdin.readline
from heapq import heappush, heappop


if __name__ == '__main__':
    N, K = map(int, input().split())
    js = []
    for _ in range(N):
        m, v = map(int, input().split())
        js.append((-v, m))
    js.sort(key=lambda x: -x[1])
    
    total = 0
    pq = []
    for c in sorted(int(input()) for _ in range(K)):
        while js and js[-1][1] <= c:
            heappush(pq, js.pop())
        if pq:
            v, _ = heappop(pq)
            total -= v
    
    print(total)
