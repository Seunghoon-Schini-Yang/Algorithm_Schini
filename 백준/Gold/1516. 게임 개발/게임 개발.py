import sys
input = sys.stdin.readline


class Dev():
    def __init__(self):
        self._calc_build_cost(int(input()))
    
    
    def _init_graph(self, N):
        graph = [[] for _ in range(N)]
        indgr = [0] * N
        cost = [0] * N
        for nn in range(N):
            c, *pn, _ = map(int, input().split())
            cost[nn] = c
            indgr[nn] += len(pn)
            for ppn in map(lambda x: x-1, pn):
                graph[ppn].append(nn)
        return graph, indgr, cost


    def _calc_build_cost(self, N):
        graph, indgr, cost = self._init_graph(N)
        btimes = [0] * N
        cands = [[0] for _ in range(N)]
        stack = [i for i in range(N) if not indgr[i]]
        while stack:
            pn = stack.pop()
            btimes[pn] = cost[pn] + max(cands[pn])
            for cn in graph[pn]:
                cands[cn].append(btimes[pn])
                indgr[cn] -= 1
                if not indgr[cn]:
                    stack.append(cn)
        self.btimes = btimes


if __name__ == '__main__':
    dev = Dev()
    print('\n'.join(map(str, dev.btimes)))
