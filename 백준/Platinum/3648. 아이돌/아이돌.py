import sys
sys.setrecursionlimit(pow(10, 9))
print = sys.stdout.write


def dfs(node: int) -> int:
    global odr, scc_num
    stack.append(node)
    cdr = odr
    rank[node] = cdr
    odr += 1

    for cn in graph[node]:
        if not rank[cn]:
            rank[node] = min(rank[node], dfs(cn))
        elif not finished[cn]:
            rank[node] = min(rank[node], rank[cn])
    
    if rank[node] == cdr:
        while True:
            cn = stack.pop()
            finished[cn] = True
            scc[cn] = scc_num
            rank[cn] = cdr
            if node == cn:
                break
        scc_num += 1

    return rank[node]


if __name__ == '__main__':
    lines = iter(sys.stdin.readlines())
    while True:
        try:
            n,m = map(int, next(lines).split())
        except StopIteration:
            break

        graph = [set() for _ in range(2*n+1)]
        # graph[-1].add(1)
        for _ in range(m):
            a,b = map(int, next(lines).split())
            graph[-a].add(b)
            graph[-b].add(a)
        
        stack = list()
        finished = [False]*(2*n+1)
        scc = [0]*(2*n+1)
        rank = [0]*(2*n+1)
        odr = scc_num = 1

        for i in range(1, 2*n+1):
            if not finished[i]:
                dfs(i)

        is_no = False
        for i in range(1, n+1):
            if scc[i] == scc[-i]:
                is_no = True
                break
        
        if is_no or scc[1] > scc[-1]:
            print('no\n')
        else:
            print('yes\n')
