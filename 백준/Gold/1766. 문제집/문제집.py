import sys
input = sys.stdin.readline
from heapq import heapify, heappush, heappop


def _pop():
    p = heappop(pq)
    for c in graph[p]:
        dgr[c] -= 1
        if not dgr[c]:
            heappush(pq, c)
    return p


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dgr = [0] * (N+1)
    for _ in range(M):
        p, c = map(int, input().split())
        graph[p].append(c)
        dgr[c] += 1
    
    pq = [i for i in range(1, N+1) if not dgr[i]]
    heapify(pq)
    print(*[_pop() for _ in range(N)])
