# Union-Find
import sys
input = sys.stdin.readline


def find(node: int) -> int:
    if node == root[node]:
        return node
    
    root[node] = find(root[node])
    return root[node]


def union(r1: int, r2: int) -> None:
    if r1 == r2:
        return

    if rank[r1] > rank[r2]:
        root[r2] = r1
    else:
        if rank[r1] == rank[r2]:
            rank[r2] += 1
        root[r1] = r2
    

if __name__ == '__main__':
    N, M = map(int, input().split())
    root = [i for i in range(N+1)]
    rank = [0 for _ in range(N+1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        union(find(n1), find(n2))

    groups = set(find(i) for i in range(1, N+1))
    print(len(groups))
