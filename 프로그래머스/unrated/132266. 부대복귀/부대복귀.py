def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for r1, r2 in roads:
        graph[r1].append(r2)
        graph[r2].append(r1)
    
    dists = [-1] * (n+1)
    dists[destination] = 0

    d = 0
    que = [destination]
    while que:
        d += 1
        tmp = []
        for q in que:
            for qq in graph[q]:
                if dists[qq] != -1:
                    continue
                dists[qq] = d
                tmp.append(qq)
        que = tmp

    return [dists[source] for source in sources]
