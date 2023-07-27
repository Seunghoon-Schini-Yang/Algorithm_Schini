import sys
input = sys.stdin.readline
from heapq import heappop, heappush


class SecondBest():
    def __init__(self, N, M):
        S, D = map(int, input().split())
        graph = [[] for _ in range(N)]
        for _ in range(M):
            U, V, P = map(int, input().split())
            graph[U].append((P, V))
        memo = [[] for _ in range(N)]

        dist = [sys.maxsize] * N
        dist[S] = 0
        pq = [(0, S)]
        while pq:
            pd, pn = heappop(pq)
            if dist[pn] < pd:
                continue
            for cd, cn in graph[pn]:
                if pd+cd < dist[cn]:
                    dist[cn] = pd+cd
                    heappush(pq, (pd+cd, cn))
                    memo[cn] = [pn]
                elif pd+cd == dist[cn]:
                    memo[cn].append(pn)

        exclude = [set() for _ in range(N)]
        stack = [(D, memo[D])]
        while stack:
            cn, pns = stack.pop()
            for pn in pns:
                if cn in exclude[pn]:
                    continue
                exclude[pn].add(cn)
                stack.append((pn, memo[pn]))

        dist = [sys.maxsize] * N
        dist[S] = 0
        pq = [(0, S)]
        while pq:
            pd, pn = heappop(pq)
            if dist[pn] < pd:
                continue
            for cd, cn in graph[pn]:
                if cn in exclude[pn]:
                    continue
                if pd+cd < dist[cn]:
                    dist[cn] = pd+cd
                    heappush(pq, (pd+cd, cn))

        self.answer = -1 if dist[D] == sys.maxsize else dist[D]
        

if __name__ == '__main__':
    while True:
        N, M = map(int, input().split())
        if N == M == 0:
            break
        tc = SecondBest(N, M)
        print(tc.answer)
