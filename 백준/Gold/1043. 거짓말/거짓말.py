import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())
    truth = [False] * (N+1)
    _, *stack = map(int, input().split())
    for i in stack:
        truth[i] = True
    
    pps = [[] for _ in range(N+1)]
    ps = []
    for i in range(M):
        _, *party = map(int, input().split())
        ps.append(party)
        for p in party:
            pps[p].append(i)
            
    while stack:
        p = stack.pop()
        for pi in pps[p]:
            for p in ps[pi]:
                if truth[p]:
                    continue
                truth[p] = True
                stack.append(p)
    
    print(sum(0 if any(truth[p] for p in party) else 1 for party in ps))
