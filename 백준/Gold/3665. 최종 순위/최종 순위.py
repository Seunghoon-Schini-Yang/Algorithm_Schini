import sys
input = sys.stdin.readline
from collections import deque


def sol(t: int) -> str:
    def case(n: int):
        degrees = [0]*(n+1)
        graph = [{} for _ in range(n+1)]
        childs = set(range(1, n+1))

        for i,v in enumerate(map(int, input().split())):
            degrees[v] = i
            childs.remove(v)
            graph[v] = childs.copy()
        
        for _ in range(int(input())):
            p,c = map(int, input().split())
            try:
                graph[c].remove(p)
                graph[p].add(c)
                degrees[p] -= 1
                degrees[c] += 1
            except KeyError:
                graph[p].remove(c)
                graph[c].add(p)
                degrees[c] -= 1
                degrees[p] += 1

        que = deque()
        for i in range(1, n+1):
            if not degrees[i]:
                que.append(i)
        # if not que:
        #     return 'IMPOSSIBLE'
        
        rank = list()
        while que:
            if len(que) > 1:
                return 'IMPOSSIBLE'
            p = que.popleft()
            rank.append(p)
            for c in graph[p]:
                degrees[c] -= 1
                if not degrees[c]:
                    que.append(c)
        
        if len(rank) < n:
            return 'IMPOSSIBLE'
        return ' '.join(map(str, rank))

    
    return '\n'.join(case(int(input())) for _ in range(t))


print(sol(int(input())))
