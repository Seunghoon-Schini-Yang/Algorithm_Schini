import sys
input = sys.stdin.readline
from heapq import heappop, heappush


class Ardenia():
    def __init__(self, n, m):
        pq = []
        lake_idx = [[] for _ in range(n+1)]
        query = list(map(int, input().split()))

        is_full = [True] * (n+1)
        for i in range(m-1, -1, -1):
            lake_idx[query[i]].append(i)
        for i in range(1, n+1):
            if lake_idx[i]:
                heappush(pq, lake_idx[i].pop())
        
        is_poss = 'YES'
        suck_up = []
        for lake in query:
            if not lake:
                if pq:
                    i = heappop(pq)
                    suck_up.append(query[i])
                    is_full[query[i]] = False
                else:
                    suck_up.append(0)
            else:
                if is_full[lake]:
                    is_poss = 'NO'
                    break
                is_full[lake] = True
                if lake_idx[lake]:
                    heappush(pq, lake_idx[lake].pop())

        self.result = (is_poss, suck_up)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        village = Ardenia(*map(int, input().split()))
        print(village.result[0])
        if village.result[0] == 'YES':
            print(*village.result[1])
